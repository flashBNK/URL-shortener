from pydantic import BaseModel, Field


class ListLinkSchema(BaseModel):
    id: int
    original_url: str
    short_url: str

class LinkSchema(ListLinkSchema):
    ...

class LinkCreateSchema(BaseModel):
    original_url: str = Field(min_length=1)
    short_url: str = Field(min_length=1)

class LinkUpdateSchema(LinkCreateSchema):
    ...