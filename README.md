# Container Bot

An example telegram bot for running in docker.

## How to use

This example requires installed **Docker** on target machine. You can always grab the latest version [here](https://get.docker.com/). You would also need **docker-compose**, which can be found [in official docs](https://docs.docker.com/compose/install/).

Next, you need to set up **docker-compose.yml** file. An example configuration:

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
    command: ./entry_point.sh
    volumes:
      - ./:/code
    depends_on:
      - db

```
You are free to choose any other database, just be sure to read instructions in official repository.

Do not forget to set up **config.py**! You need to specify telegram bot token and database credentials from docker-compose.yml. This can be done via respective environment variables or config.py can be edited directly.

You are all set! Run this command to launch your containers:
```bash
$ sudo docker-compose up -d
```

During the initial launch docker will go through building process, which can take a few minutes.

## Project Goals

The code is written for educational purposes.
