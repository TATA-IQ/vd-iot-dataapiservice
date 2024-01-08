FROM python:3.9-slim-buster as builder
RUN mkdir /app
COPY poetry.lock pyproject.toml /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

FROM python:3.9-slim-buster    
ENV PYTHONUNBUFFERED 1
COPY --from=builder /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
copy dataapiservice /app
WORKDIR /app
# RUN mkdir /app/logs
CMD ["uvicorn", "fastapp:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "5"]