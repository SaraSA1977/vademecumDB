from flask import Blueprint
from routes.dashboard import dashboard_controller

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/summary", methods=["GET"])
def get_summary():
    """
    Endpoint: GET /dashboard/summary
    Retorna resumen del dashboard (usuarios, productos, ventas, etc)
    """
    return dashboard_controller.get_summary()


@dashboard_bp.route("/sales-by-month", methods=["GET"])
def get_sales_by_month():
    """
    Endpoint: GET /dashboard/sales-by-month
    Retorna ventas por mes
    """
    return dashboard_controller.get_sales_by_month()


@dashboard_bp.route("/products-by-category", methods=["GET"])
def get_products_by_category():
    """
    Endpoint: GET /dashboard/products-by-category
    Retorna productos agrupados por categoría
    """
    return dashboard_controller.get_products_by_category()


@dashboard_bp.route("/supplier-distribution", methods=["GET"])
def get_supplier_distribution():
    """
    Endpoint: GET /dashboard/supplier-distribution
    Retorna distribución de proveedores
    """
    return dashboard_controller.get_supplier_distribution()
