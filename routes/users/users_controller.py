from flask_jwt_extended import create_access_token
 
from common.http import ok, bad_request, unauthorized, created
from routes.users import users_service
 
def login_user(data):
    ## validar controller
    user, err = users_service.login_user(data)
    if err:
        return unauthorized(message="Login Inválido", errors=err)
   
    token = create_access_token(identity=str(user.id))
 
    return ok(
        data={
            "access_token": token,
            "user": user.to_dict()
        },
        message="usuario contenido exitoso"
    )
 
def create_user(data):
    ## validar creación de usuario
    user, err = users_service.create_user(data)
    if err:
        return bad_request(message="No se pudo crear el usuario", errors=err)
    return created(data=user.to_dict(), message="Usuario creado")


def get_all_users():
    users = users_service.get_all_users()
    return ok(
        data={
            "user": [u.to_dict() for u in users]
        },
        message="Usuarios obtenidos"
    )