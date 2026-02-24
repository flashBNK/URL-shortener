from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator

def ensure_gte_zero(value: int) -> int:
    if value < 0:
        return 0
    return value

class Pagination(BaseModel):
    limit: Annotated[int, AfterValidator(ensure_gte_zero)] = Field(10, le=100)
    offset: Annotated[int, AfterValidator(ensure_gte_zero)] = 0