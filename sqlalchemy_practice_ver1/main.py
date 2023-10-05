from fastapi import FastAPI
from domain import all_router

app = FastAPI()


app.include_router(all_router.router)