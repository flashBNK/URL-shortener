from src.domain.link.repository import AbstractLinkRepository
from src.infrastructure.repositories.inmemory.link import InMemoryLinkRepository

_link_repo = InMemoryLinkRepository()

def get_link_repo() -> AbstractLinkRepository:
    return _link_repo