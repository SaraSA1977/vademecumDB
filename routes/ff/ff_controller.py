from common.http import ok, bad_request, created
from routes.ff import ff_service

def getAll():
    data, err = ff_service.getAll()
    if err:
        return bad_request(message="No se pudo obtener las formas farmacéuticas", errors=err)
    return ok(data=[d.to_dict() for d in data], message="Formas farmacéuticas obtenidas con éxito")


def createFF(data):
    result, err = ff_service.createFF(data)
    if err:
        return bad_request(message="Error creando la forma farmacéutica", errors=err)
    return created(data=result.to_dict(), message="Forma farmacéutica creada exitosamente")


def deleteFF(id: int):
    result, err = ff_service.deleteFF(id)
    if err:
        return bad_request(message="Error eliminando la forma farmacéutica", errors=err)
    return ok(data={"delete": result}, message=f"Forma farmacéutica con id {id} eliminada exitosamente")


def updateFF(id: int, data_body):
    result, err = ff_service.updateFF(id, data_body)
    if err:
        return bad_request(message="Error actualizando la forma farmacéutica", errors=err)
    return ok(data=result.to_dict(), message=f"Forma farmacéutica con id {id} actualizada exitosamente")