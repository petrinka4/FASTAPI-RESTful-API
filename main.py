from sqlalchemy import select
from fastapi import FastAPI

from models import Base,bankModel,accountModel,cityModel,filialModel,social_statusModel,clientModel,cardModel
from routers import router
from database import engine,SessionDep

app=FastAPI()



app.include_router(router)





@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok":True}






