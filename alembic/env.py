from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# --- 1. IMPORTAR SQLMODEL Y TU CONFIGURACIÓN ---
from sqlmodel import SQLModel
from app.core.config import settings

# --- 2. IMPORTAR TODOS TUS MODELOS ---
# Esto es vital. Si Alembic no "lee" los archivos de los modelos al ejecutarse, 
# va a creer que la base de datos está vacía y va a intentar borrarte las tablas.
from app.modules.hero.models import Hero
from app.modules.team.models import Team
from app.modules.weapon.models import Weapon


# this is the Alembic Config object...
config = context.config

# --- 3. SOBRESCRIBIR LA URL DE LA BASE DE DATOS ---
# Le decimos a Alembic que ignore lo que diga el archivo alembic.ini 
# y use la URL que vos ya tenés configurada en tu .env
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)


# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- 4. ASIGNAR LA METADATA ---
# Cambiamos "target_metadata = None" por la metadata de SQLModel
target_metadata = SQLModel.metadata

# ... (De acá para abajo dejas el run_migrations_offline() y online() intactos)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
