from pydantic import BaseModel


class BankAddSchema(BaseModel):
    name: str
