# FastAPI boilerplate

---

## Start project

### Local development

1. Copy .env.example to .env and fill in

2. Install poetry dependencies `poetry install`

3. Run `docker compose up --build`

---

#### Alembic (migrations)

- autogenerate migration: `poetry run alembic revision --autogenerate -m "<message>"`
- merge migrations from 0001 to the latest and generate sql script: `poetry run alembic upgrade <rev-id> --sql`
- apply migrations: `poetry run alembic upgrade head` or `make migrate`
- downgrade migration: `poetry run alembic downgrade -1` or `make downgrade`

---
