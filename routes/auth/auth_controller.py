from flask_jwt_extended import create_access_token
from common.http import ok, bad_request, unauthorized, created
from routes.auth import auth_service


def login_user(data):
    if not data:
        return bad_request(message="No se enviaron datos")

    try:
        user, err = auth_service.login_user(data)

        if err:
            return unauthorized(
                message=err.get("message")
                
            )

        token = create_access_token(identity=str(user.id))

        return ok(
            data={
                "access_token": token,
                "user": user.to_dict()
            },
            message="Login exitoso"
        )

    except Exception as e:
        print("🔥 ERROR LOGIN:", e)
        return bad_request(message=str(e))


def create_user(data):
    if not data:
        return bad_request(message="No se enviaron datos")

    try:
        user, err = auth_service.create_user(data)

        if err:
            return bad_request(
                message="No se pudo crear el usuario",
                errors=err
            )

        return created(
            data=user.to_dict(),
            message="Usuario creado correctamente"
        )

    except Exception as e:
        print("🔥 ERROR CONTROLLER:", e)
        return bad_request(message=str(e))