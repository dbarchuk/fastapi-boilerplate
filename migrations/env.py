import pathlib
from logging.config import fileConfig

from alembic import context
from alembic.script import ScriptDirectory

from app.core.db.connector import Base, async_engine, sync_engine  # noqa
from app.core.db.models.users import *  # noqa
from app.core.db.models.events import * # noqa

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = [Base.metadata, ]


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def process_revision_directives(context, revision, directives):
    # extract Migration
    migration_script = directives[0]
    # extract current head revision
    head_revision = ScriptDirectory.from_config(context.config).get_current_head()

    if head_revision is None:
        # edge case with first migration
        new_rev_id = 1
    else:
        # default branch with incrementation
        last_rev_id = int(head_revision.lstrip('0'))
        new_rev_id = last_rev_id + 1
    # fill zeros up to 4 digits: 1 -> 0001
    migration_script.rev_id = '{0:04}'.format(new_rev_id)
    if migration_script.message is None:
        migration_script.message = f"Migration {migration_script.rev_id}"


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    print("Run offline migration")
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
        process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print("Run online migrations")

    with sync_engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,

        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
