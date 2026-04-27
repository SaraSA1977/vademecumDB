
from __future__ import annotations

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, CheckConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

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


    def to_dict(self):
      return {
        "id": self.id,
        "comercial_name": self.comercial_name,
        "concentration": self.concentration
    }

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


class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True)
    sale_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    product_id = Column(Integer, ForeignKey("product_details.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), nullable=False, default="completed")
    
    def to_dict(self):
        return {
            "id": self.id,
            "sale_date": self.sale_date.isoformat() if self.sale_date else None,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "amount": float(self.amount),
            "status": self.status
        }