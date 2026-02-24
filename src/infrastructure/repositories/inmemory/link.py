from typing import List, Optional, Dict

from src.domain.link.repository import AbstractLinkRepository
from src.domain.link.models import Link, LinkCreateDTO, LinkUpdateDTO
from src.domain.link.exceptions import LinkNotFoundError

class InMemoryLinkRepository(AbstractLinkRepository):

    def __init__(self, storage: Optional[Dict[int, Link]] = None) -> None:
        self._storage: Dict[int, Link] = storage.copy() if storage else {}


    def get(self, link_id: int) -> Link:
        try:
            return self._storage[link_id]
        except KeyError:
            raise LinkNotFoundError(link_id)


    def list(self, limit: int = 100, offset: int = 0) -> List[Link]:
        links = list(self._storage.values())
        return links[offset : offset + limit]


    def create(self, dto: LinkCreateDTO) -> Link:
        if self._storage:
            last_id = list(self._storage.keys())[-1]
            next_id = last_id + 1
        else:
            next_id = 1

        link = Link(
            id=next_id,
            original_url=dto.original_url,
            short_url=dto.short_url,
        )

        self._storage[next_id] = link
        return link


    def update(self, link_id: int, dto: LinkUpdateDTO) -> Link:
        if link_id not in self._storage:
            raise LinkNotFoundError(link_id)

        existing = self._storage[link_id]
        link = Link(
            id=link_id,
            original_url=dto.original_url if dto.original_url else existing.original_url,
            short_url=dto.short_url if dto.short_url else existing.short_url,
        )

        self._storage[link_id] = link
        return link


    def delete(self, link_id: int) -> None:
        if link_id not in self._storage:
            raise LinkNotFoundError(link_id)
        del self._storage[link_id]