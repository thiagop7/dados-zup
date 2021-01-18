import abc
from abc import ABC

from modules.domain.model import TotalCost
from typing import TypeVar

T = TypeVar('T', bound='EntityBase')

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, obj: T):
        raise NotImplementedError


class TotalCostsRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, totalCost):
        self.session.add(totalCost)
