from setuptools import find_packages, setup

setup(
    name="web_app",
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

    ],
    extras_require={"dev": ["pytest"]},
)
