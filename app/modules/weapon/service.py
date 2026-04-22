from typing import List, Optional

from sqlmodel import Session, select

from app.modules.weapon.models import Weapon
from app.modules.weapon.schemas import WeaponCreate, WeaponUpdate


def create_weapon(session: Session, data: WeaponCreate) -> Weapon:
    weapon = Weapon.model_validate(data)
    session.add(weapon)
    session.commit()
    session.refresh(weapon)
    return weapon


def get_weapons(session: Session) -> List[Weapon]:
    return list(session.exec(select(Weapon)).all())


def get_weapon(session: Session, weapon_id: int) -> Optional[Weapon]:
    return session.get(Weapon, weapon_id)


def update_weapon(
    session: Session, weapon_id: int, data: WeaponUpdate
) -> Optional[Weapon]:
    weapon = session.get(Weapon, weapon_id)
    if not weapon:
        return None
    weapon_data = data.model_dump(exclude_unset=True)
    for key, value in weapon_data.items():
        setattr(weapon, key, value)
    session.add(weapon)
    session.commit()
    session.refresh(weapon)
    return weapon


def delete_weapon(session: Session, weapon_id: int) -> bool:
    weapon = session.get(Weapon, weapon_id)
    if not weapon:
        return False
    session.delete(weapon)
    session.commit()
    return True
