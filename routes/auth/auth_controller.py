from flask_jwt_extended import create_access_token
 
from common.http import ok, bad_request, unauthorized, created
from routes.auth import auth_service
 
def login_user(data):
    ## validar controller
    user, err = auth_service.login_user(data)
    if err:
        return unauthorized(message="Login Inválido", errors=err)
   
    token = create_access_token(identity=str(user.id))
 
    return ok(
        data={
            "access_token": token,
            "user": user.to_dict()
        },
        message="Login exitoso"
    )
 
def create_user(data):
    ## validar creación de usuario
    user, err = auth_service.create_user(data)
    if err:
        return bad_request(message="No se pudo crear el usuario", errors=err)
    return created(data=user.to_dict(), message="Usuario creado")