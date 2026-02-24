from abc import ABC, abstractmethod

from ..repositories.abstract import AbstractRepository
from .models import Link, LinkCreateDTO, LinkUpdateDTO
from .exceptions import LinkNotFoundError


class AbstractLinkRepository(AbstractRepository[Link, int, LinkCreateDTO, LinkUpdateDTO], ABC):

#    @abstractmethod
    ...