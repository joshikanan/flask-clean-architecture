from flask import Blueprint, Response, jsonify, make_response

from tasks.application.queries.tasks_queries import GetTasks

tasks_blueprint = Blueprint("tasks_blueprint", __name__)


@tasks_blueprint.route("/")
def task_list(query: GetTasks) -> Response:
    return make_response(jsonify(query.query()))
