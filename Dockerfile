FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.6.1

WORKDIR /usr/src
RUN mkdir "app"
WORKDIR app/
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

ENV FLASK_APP='web_app/app.py:create_app()'
CMD ["flask", "run", "--host=0.0.0.0"]


