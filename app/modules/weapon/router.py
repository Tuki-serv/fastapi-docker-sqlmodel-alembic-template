from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.modules.weapon import service
from app.modules.weapon.schemas import WeaponCreate, WeaponRead, WeaponUpdate

router = APIRouter(prefix="/weapons", tags=["weapons"])


@router.post("/", response_model=WeaponRead, status_code=201)
def create_weapon(weapon: WeaponCreate, session: Session = Depends(get_session)):
    return service.create_weapon(session, weapon)


@router.get("/", response_model=List[WeaponRead])
def list_weapons(session: Session = Depends(get_session)):
    return service.get_weapons(session)


@router.get("/{weapon_id}", response_model=WeaponRead)
def get_weapon(weapon_id: int, session: Session = Depends(get_session)):
    weapon = service.get_weapon(session, weapon_id)
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon


@router.patch("/{weapon_id}", response_model=WeaponRead)
def update_weapon(
    weapon_id: int, data: WeaponUpdate, session: Session = Depends(get_session)
):
    weapon = service.update_weapon(session, weapon_id, data)
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon


@router.delete("/{weapon_id}", status_code=204)
def delete_weapon(weapon_id: int, session: Session = Depends(get_session)):
    if not service.delete_weapon(session, weapon_id):
        raise HTTPException(status_code=404, detail="Weapon not found")
