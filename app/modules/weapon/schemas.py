from typing import Optional

from sqlmodel import SQLModel


class WeaponBase(SQLModel):
    name: str
    description: Optional[str] = None


class WeaponCreate(WeaponBase):
    pass


class WeaponRead(WeaponBase):
    id: int


class WeaponUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
