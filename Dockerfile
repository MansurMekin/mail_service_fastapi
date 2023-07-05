FROM python:3.11 as build_app


WORKDIR /app

ENV PYTHONBUFFERED 1\
    PYTHONDONTWRITEBYTECODE 1

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false

COPY . /app

FROM build_app as production

RUN poetry install --without dev

EXPOSE 8000

CMD python -m src

FROM build_app as development

RUN poetry install --with dev

EXPOSE 8000

CMD python -m src

FROM build_app as testing

RUN poetry install --with dev

EXPOSE 8000

CMD pytest -vv
