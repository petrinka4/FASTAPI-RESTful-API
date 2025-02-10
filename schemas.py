from pydantic import BaseModel

class BankAddSchema(BaseModel):
    name:str

class CityAddSchema(BaseModel):
    name:str

class FilialAddSchema(BaseModel):
    bank_id:int
    city_id:int

class Social_StatusAddSchema(BaseModel):
    name:str

class ClientAddSchema(BaseModel):
    name:str
    social_status_id:int