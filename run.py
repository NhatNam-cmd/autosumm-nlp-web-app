# run.py

from app import create_app

# Sử dụng cấu hình phát triển (DEBUG=True)
app = create_app("development")

if __name__ == "__main__":
    # host='0.0.0.0' để chạy trên mạng cục bộ và port 5000
    app.run(debug=True, host="0.0.0.0", port=5000)
