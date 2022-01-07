import os
from dataclasses import dataclass

import dotenv
import injector
from tasks.domain.entities.task_entity import Task
from sqlalchemy import MetaData
from main.modules import Db
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base(metadata=metadata)

__all__ = ["bootstrap_app"]


@dataclass
class AppContext:
    injector: injector.Injector


def bootstrap_app() -> AppContext:
    """This is bootstrap function independent from the context.

    This should be used for Web, CLI, or worker context."""
    config_path = os.environ.get(
        "CONFIG_PATH", os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, ".env_file")
    )
    dotenv.load_dotenv(config_path)
    engine = create_engine(os.environ["DB_DSN"])
    dependency_injector = _setup_dependency_injection(engine)
    _create_db_schema(engine)  # TEMPORARY

    return AppContext(dependency_injector)


def _setup_dependency_injection(engine: Engine) -> injector.Injector:
    return injector.Injector(
        [
            Db(engine),
        ],
        auto_bind=False,
    )


def _create_db_schema(engine: Engine) -> None:
    # Models has to be imported for metadata.create_all to discover them
    from tasks_infrastructure import tasks  # noqa

    # TODO: Use migrations for that
    metadata.create_all(engine)
