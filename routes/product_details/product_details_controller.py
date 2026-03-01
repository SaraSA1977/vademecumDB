from common.http import ok, bad_request, created
from routes.product_details import product_details_service

def getAll():
    data, err = product_details_service.getAll()
    if err:
        return bad_request(message="No se pudieron obtener los productos", errors=err)
    return ok(data=[d.to_dict() for d in data], message="Productos obtenidos con éxito")

def createProduct(data):
    result, err = product_details_service.createProduct(data)
    if err:
        return bad_request(message="Error creando el producto", errors=err)
    return created(data=result.to_dict(), message="Producto creado exitosamente")

def deleteProduct(id: int):
    result, err = product_details_service.deleteProduct(id)
    if err:
        return bad_request(message="Error eliminando el producto", errors=err)
    return ok(data={"delete": result}, message=f"Producto con id {id} eliminado exitosamente")

def updateProduct(id: int, data_body):
    result, err = product_details_service.updateProduct(id, data_body)
    if err:
        return bad_request(message="Error actualizando el producto", errors=err)
    return ok(data=result.to_dict(), message=f"Producto con id {id} actualizado exitosamente")