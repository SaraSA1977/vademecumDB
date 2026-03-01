from typing import Any, Dict, List, Tuple, Optional
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import FormaFarmaceutica

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def getAll() -> Tuple[List[FormaFarmaceutica], Any]:
    with get_db() as db:
        ffs = db.query(FormaFarmaceutica).all()
        return ffs, None


def createFF(data: Dict[str, Any]) -> Tuple[Optional[FormaFarmaceutica], Any]:
    try:
        with get_db() as db:
            ff = FormaFarmaceutica(name=data['name'].strip())
            db.add(ff)
            db.commit()
            db.refresh(ff)
            return ff, None
    except Exception as e:
        return None, {"error": str(e)}


def deleteFF(id: int) -> Tuple[bool, Any]:
    with get_db() as db:
        ff_exist = db.query(FormaFarmaceutica).filter(FormaFarmaceutica.id == id).first()
        if not ff_exist:
            return False, {"id": f"Forma farmacéutica con id {id} no encontrada"}
        db.delete(ff_exist)
        db.commit()
        return True, None


def updateFF(id: int, data: Dict[str, Any]) -> Tuple[Optional[FormaFarmaceutica], Any]:
    with get_db() as db:
        ff = db.query(FormaFarmaceutica).filter(FormaFarmaceutica.id == id).first()
        if not ff:
            return None, {"id": f"Forma farmacéutica con id {id} no encontrada"}
        if "name" in data:
            ff.name = data["name"].strip()
        db.commit()
        db.refresh(ff)
        return ff, None