from fastapi import FastAPI

# Importamos los routers de cada módulo
from app.modules.health.router import router as health_router
from app.modules.hero.router import router as hero_router
from app.modules.team.router import router as team_router
from app.modules.weapon.router import router as weapon_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI + SQLModel — Relaciones 1:1 · 1:N · N:M",
        version="1.0.0",
        description=(
            "Proyecto modular que demuestra las tres relaciones principales:\n\n"
            "- **1:1** Hero ↔ Weapon (FK `weapon_id` en Hero)\n"
            "- **1:N** Team → Heroes (FK `team_id` en Hero, lado N)\n"
            "- **N:M** Hero ↔ Team via `HeroTeamLink`"
        )
    )

    # Registro de Routers
    # Esto hace que aparezcan las secciones en /docs
    app.include_router(hero_router)
    app.include_router(weapon_router)
    app.include_router(health_router)
    app.include_router(team_router)
    
    return app

app = create_app()