from typing import Any, Dict, List, Tuple, Optional
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import ProductDetail

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def getAll() -> Tuple[List[ProductDetail], Any]:
    with get_db() as db:
        products = db.query(ProductDetail).all()
        return products, None


def createProduct(data: Dict[str, Any]) -> Tuple[Optional[ProductDetail], Any]:
    try:
        with get_db() as db:
            product = ProductDetail(
                comercial_name=data['comercial_name'].strip(),
                concentracion=data.get('concentracion'),
                notas=data.get('notas'),
                id_grupo=data['id_grupo'],
                id_FF=data['id_FF']
            )
            db.add(product)
            db.commit()
            db.refresh(product)
            return product, None
    except Exception as e:
        return None, {"error": str(e)}


def deleteProduct(id: int) -> Tuple[bool, Any]:
    with get_db() as db:
        product_exist = db.query(ProductDetail).filter(ProductDetail.id == id).first()
        if not product_exist:
            return False, {"id": f"Producto con id {id} no encontrado"}
        db.delete(product_exist)
        db.commit()
        return True, None


def updateProduct(id: int, data: Dict[str, Any]) -> Tuple[Optional[ProductDetail], Any]:
    with get_db() as db:
        product = db.query(ProductDetail).filter(ProductDetail.id == id).first()
        if not product:
            return None, {"id": f"Producto con id {id} no encontrado"}

        # Actualiza solo si vienen los campos en data
        if "comercial_name" in data:
            product.comercial_name = data["comercial_name"].strip()
        if "concentracion" in data:
            product.concentracion = data["concentracion"].strip()
        if "notas" in data:
            product.notas = data["notas"].strip()
        if "id_grupo" in data:
            product.id_grupo = data["id_grupo"]
        if "id_FF" in data:
            product.id_FF = data["id_FF"]

        db.commit()
        db.refresh(product)
        return product, None