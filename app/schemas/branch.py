from pydantic import BaseModel


class BranchAddSchema(BaseModel):
    bank_id: int
    city_id: int
