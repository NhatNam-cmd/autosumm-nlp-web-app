# app/__init__.py

from flask import Flask

# Import các Blueprints
from .routes import main_bp
from .api.v1.summarize import api_v1_bp


def create_app(config_name):
    app = Flask(__name__)
    # ... (Tải cấu hình từ config.py) ...

    # Đăng ký Blueprint Trang chủ
    app.register_blueprint(main_bp)

    # Đăng ký Blueprint API
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app