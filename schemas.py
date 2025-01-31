from pydantic import BaseModel

class BankAddSchema(BaseModel):
    name:str

class CityAddSchema(BaseModel):
    name:str