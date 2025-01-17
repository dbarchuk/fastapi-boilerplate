FastAPI boilerplate

---

#### Alembic (migrations)

- autogenerate migration: `$ poetry run alembic revision --autogenerate --rev-id <number> -m "<message>"`
- merge migrations from 0001 to the latest and generate sql script: `$ poetry run alembic upgrade <rev-id> --sql`
- apply migrations: `$ poetry run alembic upgrade head` or `make migrate`

---
