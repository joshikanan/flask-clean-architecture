from typing import List

from sqlalchemy.engine import RowProxy

from tasks.application.queries.tasks_queries import GetListOfTasks, TaskDto
from tasks_infrastructure.models import tasks
from tasks_infrastructure.queries.base import SqlQuery


class SqlGetListOfTasks(GetListOfTasks, SqlQuery):
    def query(self) -> List[TaskDto]:
        return [
            _row_to_dto(row) for row in self._conn.execute(tasks.select())
        ]


def _row_to_dto(task_proxy: RowProxy) -> TaskDto:
    return TaskDto(
        id=task_proxy.id,
        title=task_proxy.title,
        details=task_proxy.details,
    )
