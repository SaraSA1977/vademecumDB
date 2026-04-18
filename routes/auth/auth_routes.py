from flask import Blueprint, request
from routes.auth import auth_controller

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/create", methods=["POST"])
def create_user():
    return auth_controller.create_user(request.get_json() or {})

@auth_bp.route("/login", methods=["POST"])
def login_user():
    return auth_controller.login_user(request.get_json() or {})