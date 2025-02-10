from sqlalchemy import select
from fastapi import FastAPI

from models import Base
from routers.router_bank import router_bank
from routers.router_city import router_city
from routers.router_filial import router_filial
from routers.router_status import router_status
from routers.router_client import router_client
from database import engine

app=FastAPI()

@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok":True}


app.include_router(router_bank)
app.include_router(router_city)
app.include_router(router_filial)
app.include_router(router_status)
app.include_router(router_client)











