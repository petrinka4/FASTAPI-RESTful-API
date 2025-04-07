from pydantic import BaseModel
from typing import List, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")

class PaginationSchema(GenericModel, Generic[T]):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[T]
