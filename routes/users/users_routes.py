from flask import Blueprint, request

from routes.users import users_controller

users_bp = Blueprint("users_bp", __name__)

@users_bp.route("/getAll", methods=["GET"])
def get_all_users():
    return users_controller.get_all_users()


@users_bp.route("/create", methods=["POST"])
def create_user():
    return users_controller.create_user(request.get_json() or {})


@users_bp.route("/login", methods=["POST"])
def login_user():
    return users_controller.login_user(request.get_json() or {})