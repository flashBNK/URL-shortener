from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator

def ensure_get_zero(value: int) -> int:
    if value > 0:
        return 0
    return value

class Pagination(BaseModel):
    limit: Annotated[int, AfterValidator(ensure_get_zero)] = Field(10, le=100)
    offset: Annotated[int, AfterValidator(ensure_get_zero)] = 0