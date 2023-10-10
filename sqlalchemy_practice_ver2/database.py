import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)


# 로거(logger)를 생성하고 로깅 레벨을 설정
logger = logging.getLogger('demo')
logger.setLevel(logging.INFO)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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
