FROM python:3.10-slim-buster
ENV PYTHONPATH=/app
WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install -n

COPY main.py /app/

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]