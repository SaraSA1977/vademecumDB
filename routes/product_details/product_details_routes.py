from flask import Blueprint, request
from routes.product_details import product_details_controller

pd_bp = Blueprint("pd_bp", __name__)

@pd_bp.route("/getAll", methods=["GET"])
def getAllProducts():
    return product_details_controller.getAll()

@pd_bp.route("/createProduct", methods=["POST"])
def createProduct():
    return product_details_controller.createProduct(request.get_json() or {})

@pd_bp.route("/updateProduct/<int:id>", methods=["PUT"])
def updateProduct(id):
    return product_details_controller.updateProduct(id, request.get_json() or {})

@pd_bp.route("/deleteProduct/<int:id>", methods=["DELETE"])
def deleteProduct(id):
    return product_details_controller.deleteProduct(id)