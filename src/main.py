from fastapi import FastAPI

from src.url.router import url_router

app = FastAPI()

app.include_router(url_router)
