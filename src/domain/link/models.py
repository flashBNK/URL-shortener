from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class Link:
    id: int
    original_url: str
    short_url: str

@dataclass(slots=True)
class LinkCreateDTO:
    original_url: str
    short_url: str

@dataclass(slots=True)
class LinkUpdateDTO:
    original_url: Optional[str]
    short_url: Optional[str]