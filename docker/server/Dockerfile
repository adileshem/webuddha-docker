FROM python:3.6.3

# -- Install Pipenv:
RUN set -ex && pip install pipenv --upgrade

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --dev

COPY . /app

EXPOSE 1337

CMD ["pipenv", "run", "python", "websockets_server.py"]

# docker build -t webuddha-server-image ./docker/server/

# docker run -d --net host --name webuddha-server webuddha-server-image

# docker run --name nginx -p 8085:80 -v $PWD/docker/nginx/html:/usr/share/nginx/html:ro -d nginx