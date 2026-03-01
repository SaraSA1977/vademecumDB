from common.http import ok, bad_request, created
from routes.grupos import grupos_service  # importamos el service

def getAll():
    data, err = grupos_service.getAll()
    if err:
        return bad_request(message="No se pudo obtener los grupos", errors=err)
    return ok(data=[d.to_dict() for d in data], message="Grupos obtenidos con éxito")


def createGrupo(data):
    result, err = grupos_service.createGrupo(data)
    if err:
        return bad_request(message="Error creando el grupo", errors=err)
    return created(data=result.to_dict(), message="Grupo creado exitosamente")


def deleteGrupo(id: int):
    result, err = grupos_service.deleteGrupo(id)
    if err:
        return bad_request(message="Error eliminando el grupo", errors=err)
    return ok(data={"delete": result}, message="Grupo con id: " + str(id) + " eliminado exitosamente")


def updateGrupo(id: int, data_body):
    result, err = grupos_service.updateGrupo(id, data_body)
    if err:
        return bad_request(message="Error actualizando el grupo", errors=err)
    return ok(data=result.to_dict(), message="Grupo con id: " + str(id) + " actualizado exitosamente")