from pydantic import BaseModel


class BankAddSchema(BaseModel):
    name: str


class CityAddSchema(BaseModel):
    name: str


class BranchAddSchema(BaseModel):
    bank_id: int
    city_id: int


class Social_StatusAddSchema(BaseModel):
    name: str


class ClientAddSchema(BaseModel):
    name: str
    social_status_id: int


class AccountAddSchema(BaseModel):
    balance: int
    client_id: int
    bank_id: int


class CardAddSchema(BaseModel):
    balance: int
    account_id: int
