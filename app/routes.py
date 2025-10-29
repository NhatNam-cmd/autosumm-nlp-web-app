# app/routes.py

from flask import Blueprint, render_template

# Khởi tạo Blueprint cho trang chủ
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Trang chủ hiển thị giao diện chính"""
    # Flask sẽ tìm index.html trong thư mục app/templates
    return render_template("index.html")
