FROM python:3.9-alpine as cacher

RUN pip install pipenv

ENV WORKON_HOME=/virtualenvs

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --site-packages

FROM python:3.9-alpine as runner

COPY --from=cacher \
    /virtualenvs/*/lib/python3.9/site-packages \
    /usr/local/lib/python3.9/site-packages

WORKDIR /usr/local/src

COPY . .

EXPOSE 8000

ENTRYPOINT python3 -m uvicorn core.asgi:application \
    --forwarded-allow-ips='*' \
    --host 0.0.0.0
