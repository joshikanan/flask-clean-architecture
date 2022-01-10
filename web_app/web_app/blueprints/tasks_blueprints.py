import flask_injector
import injector
from flask import Blueprint, Response, jsonify, make_response

from tasks.application.queries.tasks_queries import GetListOfTasks
from tasks.application.use_cases.create_task import CreateTask
from tasks.application.use_cases.create_task import TaskInputDto

tasks_blueprint = Blueprint("tasks_blueprint", __name__)


class TasksWeb(injector.Module):
    @injector.provider
    @flask_injector.request
    def place_injector(self) -> None:
        return None


@tasks_blueprint.route("/")
def task_list(query: GetListOfTasks) -> Response:
    return make_response(jsonify(query.query()))


@tasks_blueprint.route("/create", methods=["POST"])
def create_task(input_dto: TaskInputDto) -> Response:
    CreateTask.execute(input_dto=input_dto)
    return make_response(jsonify({"Success": True}))
