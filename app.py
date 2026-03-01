import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# NUESTRAS RUTAS CRUD
from routes.grupos.grupos_routes import grupos_bp
from routes.ff.ff_routes import ff_bp
from routes.product_details.product_details_routes import pd_bp

from datetime import timedelta

def run_app():
    load_dotenv()
    app = Flask(__name__)

    # Configuración JWT (si luego quieres usar autenticación)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta

    # Configuración CORS
    CORS(
        resources={r"/*": {"origins": "*"}},
        supports_credentials=False,
        expose_headers=["Authorization"],
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    )

    ## registrar rutas CRUD de tus tablas
    app.register_blueprint(grupos_bp, url_prefix="/grupos")
    app.register_blueprint(ff_bp, url_prefix="/ff")
    app.register_blueprint(pd_bp, url_prefix="/products")

    return app

app = run_app()

if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 5000)),
        debug=True
    )