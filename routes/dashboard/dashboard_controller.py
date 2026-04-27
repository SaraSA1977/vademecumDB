from common.http import ok, bad_request
from routes.dashboard import dashboard_service


def get_summary():
    """
    Obtiene el resumen del dashboard
    """
    data, error = dashboard_service.get_dashboard_summary()
    print("DEBUG SUMMARY:", data, error)
    
    if error:
        return bad_request(
            message="Error al obtener resumen del dashboard",
            errors=error
        )
    
    return ok(
        data=data,
        message="Resumen del dashboard obtenido exitosamente"
    )


def get_sales_by_month():
    """
    Obtiene ventas por mes
    """
    data = dashboard_service.get_sales_by_month()
    
    return ok(
        data=data,
        message="Ventas por mes obtenidas"
    )


def get_products_by_category():
    """
    Obtiene productos por categoría
    """
    data, error = dashboard_service.get_products_by_category()
    
    if error:
        return bad_request(
            message="Error al obtener productos por categoría",
            errors=error
        )
    
    return ok(
        data=data,
        message="Productos por categoría obtenidos"
    )


def get_supplier_distribution():
    """
    Obtiene distribución de proveedores
    """
    data, error = dashboard_service.get_supplier_distribution()
    
    if error:
        return bad_request(
            message="Error al obtener distribución de proveedores",
            errors=error
        )
    
    return ok(
        data=data,
        message="Distribución de proveedores obtenida"
    )
