from flask import Blueprint, request
from routes.ff import ff_controller

ff_bp = Blueprint("ff_bp", __name__)

@ff_bp.route("/getAll", methods=["GET"])
def getAllFF():
    return ff_controller.getAll()

@ff_bp.route("/createFF", methods=["POST"])
def createFF():
    return ff_controller.createFF(request.get_json() or {})

@ff_bp.route("/updateFF/<int:id>", methods=["PUT"])
def updateFF(id):
    return ff_controller.updateFF(id, request.get_json() or {})

@ff_bp.route("/deleteFF/<int:id>", methods=["DELETE"])
def deleteFF(id):
    return ff_controller.deleteFF(id)