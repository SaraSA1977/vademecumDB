
from __future__ import annotations

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import relationship

from db.db import Base
#grrupo
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
    concentracion = Column(String(100))
    notas = Column(String)




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
        "concentracion": self.concentracion,
        "notas": self.notas,
        "id_grupo": self.id_grupo,
        "id_FF": self.id_FF
    }





    # Relaciones
    grupo = relationship("Grupo")
    forma_farmaceutica = relationship("FormaFarmaceutica")
    