# app/api/v1/summarize.py

from flask import Blueprint, request, jsonify

# Khởi tạo Blueprint API
api_v1_bp = Blueprint("api_v1", __name__)


@api_v1_bp.route("/summarize", methods=["POST"])
def summarize():
    # 1. NHẬN DỮ LIỆU JSON (thay vì request.form)
    data = request.get_json()

    # 2. Xử lý Validation (Backend Lead sẽ triển khai logic này sau)
    if not data or "text" not in data:
        return (
            jsonify(
                {"error": {"code": "invalid_input", "message": "Text is required."}}
            ),
            400,
        )

    # ... (Các Mock Logic và tính toán Stats từ file cũ) ...
    mock_summary = "Đây là một bản tóm tắt mẫu..."  # Mock data cũ

    # 3. Trả về JSON theo API Contract đã thống nhất
    return jsonify(
        {
            "summary": mock_summary.strip(),
            "meta": {
                # Sử dụng các trường meta đã thống nhất (original_length, v.v.)
                "original_length": 500,
                "summary_length": 120,
                "sentences": data.get("max_sentences", 3),
            },
        }
    )
