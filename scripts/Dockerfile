FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install pipenv

RUN pipenv --python 3.10 install --deploy --ignore-pipfile

ENTRYPOINT ["python3"]