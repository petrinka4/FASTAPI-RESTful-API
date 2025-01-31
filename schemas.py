from pydantic import BaseModel

class BankAddSchema(BaseModel):
    name:str

class CityAddSchema(BaseModel):
    name:str

class FilialAddSchema(BaseModel):
    bank_id:int
    city_id:int