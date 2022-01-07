import abc
from dataclasses import dataclass
from typing import List


@dataclass
class TaskDto:
    id: int
    title: str
    details: str


class GetTasks(abc.ABC):
    @abc.abstractmethod
    def query(self) -> List[TaskDto]:
        pass
