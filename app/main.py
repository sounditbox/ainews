from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import engine, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        init_db()
        yield
    finally:
        engine.dispose()


def create_app() -> FastAPI:
    return FastAPI(lifespan=lifespan)


app = create_app()
