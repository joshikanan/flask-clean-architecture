from setuptools import find_packages, setup

setup(
    name="tasks_infrastructure",
    version="0.0.0",
    packages=find_packages(),
    install_requires=["injector", "pytz", "sqlalchemy", "foundation"],
    extras_require={"dev": ["pytest"]},
)
