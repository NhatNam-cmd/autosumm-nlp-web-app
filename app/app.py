from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Trang chủ hiển thị giao diện chính"""
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    """
    Endpoint để xử lý tóm tắt văn bản
    Hiện tại chỉ trả về mock data để test giao diện
    """
    text = request.form.get('text', '')
    length = request.form.get('length', 'medium')
    summary_type = request.form.get('type', 'extractive')
    
    # Mock response để test giao diện
    # Sau này sẽ thay thế bằng logic tóm tắt thực tế
    mock_summary = """
    Đây là một bản tóm tắt mẫu để test giao diện. 
    Trong phiên bản thực tế, đoạn văn bản này sẽ được thay thế 
    bằng kết quả tóm tắt từ thuật toán NLP sử dụng thư viện NLTK. 
    Hệ thống sẽ phân tích văn bản đầu vào, tính điểm cho từng câu 
    dựa trên các yếu tố như tần suất từ khóa, vị trí trong đoạn văn, 
    và độ quan trọng của câu, sau đó chọn ra những câu có điểm cao nhất 
    để tạo thành bản tóm tắt cuối cùng.
    """
    
    # Thống kê mẫu
    original_words = len(text.split()) if text else 0
    summary_words = len(mock_summary.split())
    compression_ratio = round((1 - summary_words/original_words) * 100, 1) if original_words > 0 else 0
    
    return jsonify({
        'success': True,
        'summary': mock_summary.strip(),
        'stats': {
            'original_words': original_words,
            'summary_words': summary_words,
            'compression_ratio': compression_ratio
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
