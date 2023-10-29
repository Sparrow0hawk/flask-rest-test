FROM python:3.11-slim

ENV PORT 5000

WORKDIR /usr/src/app
COPY . .
COPY pyproject.toml .

RUN pip install --no-cache-dir .

CMD [ "sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --timeout 0 'flask_rest_test:create_app()'" ]
