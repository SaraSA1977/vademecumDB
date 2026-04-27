
from __future__ import annotations

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import relationship

from db.db import Base
 #grrupo



class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Grupo(Base):
    __tablename__ = "grupos"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    products = relationship(
        "ProductDetail",
        back_populates="grupo",
        passive_deletes=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    

#forma farmaceutica
class FormaFarmaceutica(Base):
    __tablename__ = "forma_farmaceutica"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)

    products = relationship(
        "ProductDetail",
        back_populates="forma_farmaceutica",
        passive_deletes=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    

#productDetail
class ProductDetail(Base):
    __tablename__ = "product_details"

    id = Column(Integer, primary_key=True)

    comercial_name = Column(String(200), nullable=False)
    concentration = Column(String(100))




    id_grupo = Column(
        Integer,
        ForeignKey("grupos.id", ondelete="RESTRICT"),
        nullable=False
    )


    id_FF = Column(
        Integer,
        ForeignKey("forma_farmaceutica.id", ondelete="RESTRICT"),
        nullable=False
    )


    def to_dict(self):
      return {
        "id": self.id,
        "comercial_name": self.comercial_name,
        "concentration": self.concentration,
        "id_grupo": self.id_grupo,
        "id_FF": self.id_FF
    }





    # Relaciones
    grupo = relationship("Grupo")
    forma_farmaceutica = relationship("FormaFarmaceutica")

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    identification = Column(String(15), nullable=False, unique = True)
    email = Column(String(100), nullable=True, unique = True)
    full_name = Column(String(200), nullable=False)
    password_hash = Column(String(200), nullable=False)
    is_active = Column(Integer, nullable=False, default=1)

    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("Role")

    def to_dict(self):
        return{
            "id":self.id,
            "identification" : self.identification,
            "email" : self.email,
            "full_name" : self.full_name,
            "is_active" : self.is_active,
            "role_id": self.role_id

        }
    