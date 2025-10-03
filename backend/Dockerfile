from python:3.12-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
COPY . /code

RUN uv pip install --system .
