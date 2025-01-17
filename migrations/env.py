import pathlib
from logging.config import fileConfig

from alembic import context

from app.core.db.connector import Base, async_engine, sync_engine
from app.core.models.users import *  # noqa

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [Base.metadata, ]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    MIGRATIONS_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_VERSIONS_DIR = MIGRATIONS_DIR / "sql_versions"

    sql_versions_dir = pathlib.Path(SQL_VERSIONS_DIR)
    if not sql_versions_dir.exists():
        sql_versions_dir.mkdir()

    # url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=async_engine.url,
        target_metadata=target_metadata,
        literal_binds=True,
        output_buffer=open(SQL_VERSIONS_DIR / f"{context.get_head_revision()}.sql", "w"),
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    with sync_engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
