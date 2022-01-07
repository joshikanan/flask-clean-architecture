from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import MetaData

metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("details", String(255), nullable=False),
)
