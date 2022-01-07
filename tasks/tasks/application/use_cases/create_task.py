from dataclasses import dataclass

from tasks.application.repositories.tasks_base_repo import TaskBaseRepository
from tasks.domain.entities.task_entity import Task
from tasks.domain.value_objects import TaskId


@dataclass
class TaskInputDto:
    task_id: TaskId
    title: str
    details: str


class CreateTask:
    def __init__(self, task_repo: TaskBaseRepository) -> None:
        self.task_repo = task_repo

    def execute(self, input_dto: TaskInputDto) -> None:
        # add validations if any

        task_data = Task.create(input_dto.task_id, input_dto.title, input_dto.details)
        self.task_repo.save(task_data)
