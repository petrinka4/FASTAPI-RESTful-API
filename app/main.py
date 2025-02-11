from fastapi import FastAPI

from app.models.base import Base
from app.routers.router_account import router_account
from app.routers.router_bank import router_bank
from app.routers.router_city import router_city
from app.routers.router_filial import router_filial
from app.routers.router_status import router_status
from app.routers.router_client import router_client
from app.routers.router_card import router_card
from app.database import engine

app = FastAPI()

#drop and create db
@app.get("/")
def root():
    return{"hi":"nigga"}

@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}


app.include_router(router_bank)
app.include_router(router_city)
app.include_router(router_filial)
app.include_router(router_status)
app.include_router(router_client)
app.include_router(router_account)
app.include_router(router_card)
