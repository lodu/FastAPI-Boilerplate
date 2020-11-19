# Boilerplate for [FastAPI](https://fastapi.tiangolo.com/)

> Important
>
> - Passwords are not actually getting hashed.
> - All origins are allowed
> - You might need to set `$PYTHONPATH` (to **parentfolder** of [src](./src) so probably [here](./))

# Docker

## Setting up

### Postgresql

- `docker volume create postgres-data` for persistence of database
- Create table `users` and dummydata: see [scripts.py](./src/database/scripts.py) for simple function(s)
  - this can be done from either inside (Docker) container or from outside ofcourse.

### Optional: Alembic

- `pip install alembic`
- `alembic init alembic`
- set URL in alembic.ini
- for `--autogenerate`, set `target_metadata` in alembics `env.py` like this:

```
import sys

sys.path = ['', '..'] + sys.path[1:]

from src.database import Base
from src.database.models import User
target_metadata = Base.metadata
```

# Python (without Docker)

### Well, thats a lie, we will still use docker for a postgres-database

> Tested on Python 3.7+

- Create virtual env and activate it.
- `pip install -r requirements.txt`
- To run api: `uvicorn main:app`

  - optionally you can add `--reload` for watch functionality

## docker-compose

- Make comment of/Remove the services of `api` and `proxy` in [docker-compose.yaml](./docker-compose.yaml)

## Postgres

- `docker volume create postgres-data` for persistence of database
- `docker-compose up` to run db.

# Default config

Change default configs in:

- [database/\_\_init\_\_.py](./src/database/__init__.py)
- [Dockerfile](./Dockerfile)
- [docker-compose.yaml](./docker-compose.yaml)
