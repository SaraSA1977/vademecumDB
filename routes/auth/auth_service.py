from typing import Any, Tuple, Dict, Optional
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


# 🔐 LOGIN CON EMAIL
def login_user(data) -> Tuple[Optional[User], Any]:

    email = (data.get("email") or "").strip()
    password = (data.get("password") or "").strip()

    if not email or not password:
        return None, {"message": "Correo y contraseña son requeridos"}

    with get_db() as db:
        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None, {"message": "Usuario no encontrado"}

        if not user.is_active:
            return None, {"message": "Usuario inactivo"}

        if not check_password_hash(user.password_hash, password):
            return None, {"message": "Contraseña incorrecta"}

        return user, None


# 🆕 REGISTRO CON EMAIL
def create_user(data: Dict[str, Any]) -> Tuple[Optional[User], Any]:

    identification = (data.get("identification") or "").strip()
    password = data.get("password") or ""
    full_name = (data.get("full_name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    telephone = (data.get("telephone") or "").strip()

    # 🔥 VALIDAR CAMPOS
    if not email or not password:
        return None, {"message": "Email y contraseña son requeridos"}

    try:  # 👈 AQUÍ EMPIEZA EL TRY

        with get_db() as db:

            # 🔥 VALIDAR SI YA EXISTE EL EMAIL
            exists = db.query(User).filter(User.email == email).first()
            if exists:
                return None, {"message": "Este correo ya está registrado"}

            # 🔥 REGLAS DE ROLES
            if email == "admin@gmail.com":
                role_id = 1  # 👑 ADMIN

            elif email.endswith("@uces.edu.co"):
                role_id = 2  # 👤 USUARIO NORMAL

            else:
                return None, {"message": "Solo se permiten correos @uces.edu.co o el admin"}

            # 🔥 CREAR USUARIO
            user = User(
                identification=identification,
                full_name=full_name,
                email=email,
                password_hash=generate_password_hash(password),
                role_id=role_id
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            return user, None

    except Exception as e:  # 👈 AHORA SÍ ES VÁLIDO
        print("🔥 ERROR REAL:", e)
        return None, {"message": str(e)}