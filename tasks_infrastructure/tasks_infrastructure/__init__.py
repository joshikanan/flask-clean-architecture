import injector
from sqlalchemy.engine import Connection

from tasks.application.queries.tasks_queries import GetListOfTasks
from tasks_infrastructure.models import tasks
from tasks_infrastructure.queries.tasks_queries import SqlGetListOfTasks
from tasks_infrastructure.repositories.task_repo import TasksRepository

__all__ = [
    # module
    "TasksInfrastructure",
    # models
    "tasks",

]


class TasksInfrastructure(injector.Module):
    @injector.provider
    def get_tasks(self, conn: Connection) -> GetListOfTasks:
        return SqlGetListOfTasks(conn)
