# Webuddha client-server - Dockerized

## Intro
This is a dockerized version of the [webuddha](https://github.com/OwnHealthIL/webuddha) repository.

This repository contains code files for initializing and running 2 dockers:

    * Webuddha server
    * Nginx


## Nginx docker

Create the `nginx` container via:

    docker run --name nginx -p 8085:80 -v $PWD/docker/nginx/html:/usr/share/nginx/html:ro -d nginx

## Server docker

First, create `webuddha-server-image` via:

    docker build -t webuddha-server-image ./docker/server/
    
Or, download it from [Dockerhub](https://hub.docker.com) via `docker pull adile/webuddha-server-image`.


You can verified  the image was created by running `docker images`.

Now, the `webuddha-server` container can be created, based on the image.

Run:

    docker run -d --net host --name webuddha-server webuddha-server-image
    


## Running the client

You can access the client via [http://localhost:8085](http://localhost:8085).


