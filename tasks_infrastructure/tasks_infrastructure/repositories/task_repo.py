from sqlalchemy.engine import Connection

from tasks.application.repositories.tasks_base_repo import TaskBaseRepository
from tasks.domain.entities.task_entity import Task
from tasks.domain.value_objects import TaskId
from tasks_infrastructure import tasks


class TasksRepository(TaskBaseRepository):
    def __init__(self, connection: Connection) -> None:
        self._conn = connection

    def get(self, task_id: TaskId) -> Task:
        row = self._conn.execute(tasks.select().where(tasks.c.id == task_id)).first()
        if not row:
            raise Exception("Not found")
        return Task(
            row.id,
            row.title,
            row.details,
        )
