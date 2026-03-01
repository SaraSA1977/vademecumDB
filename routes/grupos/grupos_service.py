from typing import Any, Dict, List, Tuple, Optional
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import Grupo

# ---------------- Sesión DB ----------------
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- Get All ----------------
def getAll() -> Tuple[List[Grupo], Any]:
    with get_db() as db:
        grupos = db.query(Grupo).all()
        return grupos, None

# ---------------- Create ----------------
def createGrupo(data: Dict[str, Any]) -> Tuple[Optional[Grupo], Any]:
    try:
        with get_db() as db:
            g = Grupo(name=data['name'].strip())
            db.add(g)
            db.commit()
            db.refresh(g)
            return g, None
    except Exception as e:
        return None, {"error": str(e)}

# ---------------- Delete ----------------
def deleteGrupo(id: int) -> Tuple[bool, Any]:
    with get_db() as db:
        grupo_exist = db.query(Grupo).filter(Grupo.id == id).first()
        if not grupo_exist:
            return False, {"id": f"Grupo con id {id} no encontrado"}
        db.delete(grupo_exist)
        db.commit()
        return True, None

# ---------------- Update ----------------
def updateGrupo(id: int, data: Dict[str, Any]) -> Tuple[Optional[Grupo], Any]:
    with get_db() as db:
        g = db.query(Grupo).filter(Grupo.id == id).first()
        if not g:
            return None, {"id": f"Grupo con id {id} no encontrado"}
        # Actualiza solo si viene el campo "name"
        if "name" in data:
            g.name = data["name"].strip()
        db.commit()
        db.refresh(g)
        return g, None