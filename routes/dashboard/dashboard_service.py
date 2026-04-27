from db.db import SessionLocal
from db.models import User, ProductDetail, Grupo


def get_dashboard_summary():
    """
    Obtiene un resumen del dashboard con datos reales de la BD
    """
    session = SessionLocal()
    try:
        # 🔹 Total usuarios (SIN usar is_active para evitar errores)
        total_users = session.query(User).count()

        # 🔹 Total productos
        total_products = session.query(ProductDetail).count()

        # 🔹 Ventas (placeholder)
        total_sales = 0

        # 🔹 % usuarios activos (si NO tienes campo is_active, dejamos 100)
        active_users_percent = 100

        return {
            "totalUsers": total_users,
            "totalProducts": total_products,
            "totalSales": total_sales,
            "activeUsersPercent": active_users_percent
        }, None

    except Exception as e:
        return None, str(e)
    finally:
        session.close()


def get_sales_by_month():
    """
    Datos de ejemplo (hasta que tengas tabla de ventas)
    """
    return {
        "labels": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
        "data": [12, 19, 30, 25, 20, 28]
    }


def get_products_by_category():
    """
    Productos por categoría (datos de ejemplo)
    """
    return {
        "labels": ["Antibióticos", "Analgésicos", "Vitaminas", "Antiinflamatorios"],
        "data": [40, 28, 35, 22]
    }


def get_supplier_distribution():
    """
    Distribución (temporal usando grupos)
    """
    session = SessionLocal()
    try:
        grupos = session.query(Grupo).limit(3).all()

        labels = [g.name for g in grupos]

        # Datos de ejemplo coherentes con cantidad
        data = [40, 35, 25][:len(labels)] if labels else [100]

        return {
            "labels": labels if labels else ["Sin datos"],
            "data": data
        }, None

    except Exception as e:
        return None, str(e)
    finally:
        session.close()