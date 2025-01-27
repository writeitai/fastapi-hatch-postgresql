# fastapi-hatch-postgresql

## Technologies
- FastAPI
- Hatch
- PostgreSQL
- async SQLAlchemy + Alembic
- docker compose
- special Docker and docker compose setup for WritIt.ai

## Prerequisites
- Hatch
  - install [Hatch](https://hatch.pypa.io/latest/install)
  - [optional] the dependencies are installed outside of the current project. This might be inconvenient due to IDE setup. You can change this behaviour by editing Hatch's `config.toml`.
    - the `config.toml` can be found [here](https://hatch.pypa.io/latest/config/hatch/#hatch-configuration) 
    - it should contain following:
    ```
    [dirs.env]
    virtual = "virtualenvs"
    ```
    
## First run
- `docker compose up -d`
- `hatch run makemigrations`
- `hatch run migrate`
- `hatch run runserver`

## Run
- database: `docker compose up -d`
- development server: `hatch run runserver`
- unit tests: `hatch run test:unit`
- generate migrations: `hatch run makemigrations`
- apply migrations: `hatch run migrate`

## When integrating to WriteIt.ai
The [WriteIt.ai](https://writeit.ai) docker setup expects following:
- `/writeitai.Dockerfile` for Dockerfile
- `/writeitai.compose.yml` for docker compose file
- `cd src && python -m pytest` for Command for running unit tests
- `tests/test_endpoint.py` for Test File