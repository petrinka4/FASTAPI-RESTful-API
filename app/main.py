from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.models.base import Base
from app.routers.account import router_account
from app.routers.bank import router_bank
from app.routers.city import router_city
from app.routers.branch import router_branch
from app.routers.status import router_status
from app.routers.client import router_client
from app.routers.card import router_card
from app.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(router_bank)
app.include_router(router_city)
app.include_router(router_branch)
app.include_router(router_status)
app.include_router(router_client)
app.include_router(router_account)
app.include_router(router_card)
