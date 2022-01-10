import injector
from tasks.domain.value_objects import TaskId

from tasks.application.repositories.tasks_base_repo import TaskBaseRepository
from tasks.application.use_cases.create_task import CreateTask
__all__ = [
    # module
    "Tasks",
    # value objects
    "TaskId",

]


class Tasks(injector.Module):
    @injector.provider
    def creating_tasks(self, repo: TaskBaseRepository) -> CreateTask:
        return CreateTask(repo)