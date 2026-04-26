from python:3.12-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
COPY . /code
WORKDIR /code
RUN uv pip install --system .
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]