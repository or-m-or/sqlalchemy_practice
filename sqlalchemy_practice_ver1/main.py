from fastapi import FastAPI
from domain import all_router
# alembic 없이 테이블 생성
# 데이터베이스에 테이블이 존재하지 않을 경우에만 테이블을 생성한다. 
# 한번 생성된 테이블에 대한 변경 관리를 할 수는 없다
# import models
# from database import engine
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(all_router.router)