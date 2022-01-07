from setuptools import find_packages, setup

setup(
    name="sunrise_diamonds",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask-Security",
        "Flask-Injector",
        "Flask",
        "bcrypt",
        "marshmallow",
        "sqlalchemy",
        "main",
        "tasks",
        "tasks_infrastructure",
        "web_app"
    ],
    extras_require={"dev": ["pytest"]},
)
