from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api import api
from app.database import engine
from app.error_handling import register_error_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(api)
register_error_handlers(app)

