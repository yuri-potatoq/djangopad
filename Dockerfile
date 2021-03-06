FROM python:3.9 as cacher

RUN pip install pipenv

ENV WORKON_HOME=/virtualenvs

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --site-packages

FROM python:3.9 as runner

COPY --from=cacher \
    /virtualenvs/*/lib/python3.9/site-packages \
    /usr/local/lib/python3.9/site-packages

WORKDIR /usr/local/src

COPY . .

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

ENTRYPOINT python3 runner.py
