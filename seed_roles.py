from db.db import SessionLocal
from db.models import Role

db = SessionLocal()

# Verificamos si ya existen para no duplicar
if not db.query(Role).filter(Role.id == 1).first():
    db.add(Role(id=1, name="admin"))

if not db.query(Role).filter(Role.id == 2).first():
    db.add(Role(id=2, name="usuario"))

db.commit()
db.close()

print("Roles creados correctamente")