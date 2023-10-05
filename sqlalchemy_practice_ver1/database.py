import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging


SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)

# 로그 설정을 초기화, 기본 로그 레벨 및 출력 포맷을 설정하는 데 사용
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# 로거(logger)를 생성하고 로깅 레벨을 설정
logger = logging.getLogger('demo')
logger.setLevel(logging.INFO)

# sqlalchemy.engine 레벨 INFO : Query 로깅, DEBUG : Query+결과 로깅
# sqlalchemy.dialects controls custom logging for SQL dialects.
# sqlalchemy.pool 레벨을 INFO 이하로 해두면 connection pool의 checkouts/checkins 을 로깅한다.
# sqlalchemy.orm 레벨을 INFO로 해두면 mapper confineration들을 로깅한다.





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
