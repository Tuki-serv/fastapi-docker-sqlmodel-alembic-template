from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.database import engine

# Importar modelos para registrarlos
from app.modules.team.models import Team
from app.modules.hero.models import Hero
from app.modules.weapon.models import Weapon

# Forma facil de crear las tablas en la base de datos
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     SQLModel.metadata.create_all(engine)
#     yield

# app = FastAPI(lifespan=lifespan)

app = FastAPI()