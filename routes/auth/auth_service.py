from typing import Any, List, Tuple, Dict, Optional
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import User
 
from werkzeug.security import check_password_hash, generate_password_hash
 
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
def login_user(data) -> Tuple[Optional[User], Any]:
    identification = data.get("identification" or "")
    password = data.get("password" or "")
    identification = identification.strip()
    password = password.strip()
 
    if not identification or not password:
        return None, {"Credenciales": "Cédula y contraseña son requeridas"}
   
    with get_db() as db:
        user = db.query(User).filter(User.identification == identification).first()
        if not user:
            return None, {"message": "usuario no encontrado en la DB"}
        if not user.is_active:
            return None, {"message": "usuario inactivo"}
        if not check_password_hash(user.password_hash, password):
            return None, {"message": "password incorrecto, intente de nuevo"}
        return user, None
 
def create_user(data: Dict[str, Any]) -> Tuple[Optional[User], Any]:
    """Útil para pruebas (semilla). Crea un usuario con contraseña hasheada."""
    identification = (data.get("identification") or "").strip()
    password = data.get("password") or ""
    full_name = (data.get("full_name") or "").strip()
 
    if not identification or not password:
        return None, {"identification/password": "identification y password son requeridos"}
 
    with get_db() as db:
        exists = db.query(User).filter(User.identification == identification).first()
        if exists:
            return None, {"identification": "Ya existe un usuario con esa cédula"}
 
        user = User(
            identification=identification,
            full_name=full_name,
            password_hash=generate_password_hash(password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user, None