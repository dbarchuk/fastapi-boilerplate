migrate:
	poetry run alembic upgrade head

downgrade:
	poetry run alembic downgrade -1

fix:
	poetry run ruff check --fix
