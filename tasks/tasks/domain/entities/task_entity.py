from tasks.domain.value_objects import TaskId


class Task:
    def __init__(
            self, id: TaskId, title: str, details: str
    ) -> None:
        super().__init__()
        self.id = id
        self.title = title
        self.details = details

    @classmethod
    def create(cls, id: TaskId, title: str, details: str) -> "Task":
        task = Task(id, title, details)
        # auction._record_event(AuctionBegan(id, starting_price, title)) Unable to understand : TBD
        return task

    def __str__(self) -> str:
        return f'<Task #{self.id}>'
