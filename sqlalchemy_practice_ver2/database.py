import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
user_router.py에서 user_list함수의 매개변수로 db: Session = Depends(get_db) 객체를 주입 받음.
db: Session 은 db객체가 Session 타입임을 의미함
Fastapi의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 반환함.
따라서 db: Session = Depends(get_db)의 db 객체에는 get_db 제너레이터에 의해 생성된 세션 객체가 주입된다. 
이 때 get_db 함수에 자동으로 contextmanager가 적용되기 때문에(Depends에서 contextmanager를 적용하게끔 설계되어 있다.) 
database.py의 get_db 함수는 다음과 같이 적용한 @contextlib.contextmanager 어노테이션을 제거해야 한다.
"""

def get_db(): # db세션 객체를 반환하는 제너레이터인 get_db함수
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()


# # Dpendency Injection(의존성 주입) : db 세션 객체를 생성하고 종료하는 반복적인 작업 (db.close())를 깔끔하게 처리
# @contextlib.contextmanager
# def get_db(): # db세션 객체를 반환하는 제너레이터인 get_db함수
#     db = SessionLocal() 
#     try:
#         yield db
#     finally:
#         db.close()
