# Container Bot

An example telegram bot for running in docker.

## How to use

This example requires installed *Docker* on target machine. You can always grab the latest version [here](https://get.docker.com/). You would also need *docker-compose*, which can be found [in official docs](https://docs.docker.com/compose/install/).

Next, you need to set up *docker-compose.yml* file. An example configuration:

```yml
version: '3'
services:

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: YOUR_PASSWORD_HERE
      POSTGRES_USER: USERNAME_HERE
      POSTGRES_DB: DB_NAME_HERE
    volumes:
      - /var/lib/postgresql/data:/var/lib/postgresql/data

  cc-bot:
    build: .
    command: python bot.py
    volumes:
      - ./:/code
    depends_on:
      - db

```

Do not forget to set up *config.py*! You need to specify database credentials from docker-compose.yml and telegram bot token. This can be done via respective environmental variables or can config.py can be edited directly.

You are all set! Run this command to run your containers:
```bash
$ sudo docker-compose up -d
```

During the first launch docker will go through building process, which can take a few minutes.

## Project Goals

The code is written for educational purposes.
