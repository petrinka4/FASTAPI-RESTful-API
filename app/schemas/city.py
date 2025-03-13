from pydantic import BaseModel


class CityAddSchema(BaseModel):
    name: str
