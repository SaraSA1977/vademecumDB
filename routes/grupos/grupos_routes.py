from flask import Blueprint, request
from routes.grupos import grupos_controller

grupos_bp = Blueprint("grupos_bp", __name__)

@grupos_bp.route("/getAll", methods=["GET"])
def getAllGrupos():
    return grupos_controller.getAll()

@grupos_bp.route("/createGrupo", methods=["POST"])
def createGrupo():
    return grupos_controller.createGrupo(request.get_json() or {})

@grupos_bp.route("/updateGrupo/<int:id>", methods=["PUT"])
def updateGrupo(id):
    return grupos_controller.updateGrupo(id, request.get_json() or {})

@grupos_bp.route("/deleteGrupo/<int:id>", methods=["DELETE"])
def deleteGrupo(id):
    return grupos_controller.deleteGrupo(id)