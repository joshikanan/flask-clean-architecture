import abc

from tasks.domain.entities.task_entity import Task
from tasks.domain.value_objects import TaskId


class TaskBaseRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, task_id: TaskId) -> Task:
        pass

    @abc.abstractmethod
    def save(self, task_id: TaskId) -> None:
        pass
