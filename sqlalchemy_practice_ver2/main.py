from fastapi import FastAPI
from domain import all_router

app = FastAPI()


# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

app.include_router(all_router.router)