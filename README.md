# AutoSumm: Ứng Dụng Web Tóm Tắt Văn Bản Tự Động

## 📝 Giới thiệu Dự án

**AutoSumm** là một ứng dụng web được xây dựng bằng **Python** và framework **Flask**, cung cấp khả năng **tóm tắt văn bản tự động**.

Dự án không chỉ tập trung vào việc tạo ra một công cụ thực tiễn mà còn là minh chứng cho năng lực của nhóm trong việc phát triển **full-stack** và áp dụng các quy trình kỹ thuật phần mềm chuyên nghiệp vào lĩnh vực **Xử lý Ngôn ngữ Tự nhiên (NLP)**.

Toàn bộ ứng dụng được thiết kế và phát triển trong khung thời gian **12 tuần**.

---

## ✨ Tính năng

### 🎯 Sản phẩm Khả dụng Tối thiểu (MVP)

Phạm vi cốt lõi của dự án tập trung vào việc hoàn thành một Sản phẩm Khả dụng Tối thiểu (**MVP**) hoạt động ổn định:

- **Giao diện Người dùng Tối giản:** Một giao diện web đơn trang với vùng nhập liệu (`<textarea>`) và khu vực hiển thị kết quả.
    
- **Tóm tắt Trích xuất:** Triển khai thuật toán **tóm tắt trích xuất (extractive summarization)** cơ bản nhưng hiệu quả, sử dụng thư viện **NLTK** để chấm điểm câu dựa trên tần suất từ và chọn ra những câu quan trọng nhất.
    
- **Backend API:** Một điểm cuối (endpoint) API đơn giản, sử dụng phương thức `POST` để nhận văn bản thô và trả về văn bản đã được tóm tắt dưới dạng **JSON**.
    
- **Triển khai Công khai:** MVP được triển khai thành công trên một nền tảng lưu trữ miễn phí (PythonAnywhere/Render) và có thể truy cập công khai thông qua URL.
    

### 🚀 Mục tiêu Mở rộng (Stretch Goals)

Các tính năng nâng cao, sẽ được xem xét và thực hiện sau khi MVP đã hoàn thành và triển khai thành công:

- **Tùy chỉnh Độ dài:** Thêm tùy chọn cho phép người dùng kiểm soát độ dài của bản tóm tắt (số câu hoặc tỷ lệ phần trăm).
    
- **Tóm tắt từ URL:** Cho phép người dùng nhập một URL để hệ thống tự động lấy nội dung bài báo và thực hiện tóm tắt.
    
- **Mô hình Tiên tiến:** Nghiên cứu và tích hợp các mô hình **Transformer** (ví dụ: PEGASUS) từ Hugging Face để thực hiện **tóm tắt trừu tượng (abstractive summarization)**.
    
- **Tài khoản & Lịch sử:** Triển khai chức năng đăng ký/đăng nhập để người dùng có thể lưu lại lịch sử các lần tóm tắt.
    

---

## 🏗️ Kiến trúc Hệ thống

Dự án áp dụng mô hình **Kiến trúc Ba Tầng (Three-Tier Architecture)** để đảm bảo tính module, khả năng bảo trì và mở rộng.

1. **Tầng Trình bày (Presentation Tier):**
    
    - **Mục đích:** Giao diện người dùng.
        
    - **Công nghệ:** HTML5, CSS3, JavaScript thuần.
        
2. **Tầng Logic (Logic Tier):**
    
    - **Mục đích:** Bộ não của ứng dụng, xử lý yêu cầu HTTP, xác thực dữ liệu.
        
    - **Công nghệ:** Framework **Flask** (Python).
        
3. **Tầng Dịch vụ (NLP Service Tier):**
    
    - **Mục đích:** Module Python riêng biệt chứa toàn bộ logic cốt lõi của việc tóm tắt văn bản.
        
    - **Công nghệ:** **NLTK** (MVP).
        

---

## 🛠️ Ngăn xếp Công nghệ (Tech Stack)

|Hạng mục|Công nghệ|Lý do lựa chọn chính|
|---|---|---|
|**Ngôn ngữ Lập trình**|`Python 3.9+`|Hệ sinh thái mạnh mẽ cho web và NLP.|
|**Framework Backend**|`Flask`|Nhẹ, dễ học và linh hoạt cho dự án quy mô vừa và nhỏ.|
|**Thư viện NLP (MVP)**|`NLTK`|Lý tưởng để triển khai các thuật toán nền tảng (tóm tắt trích xuất).|
|**Frontend**|`HTML5, CSS3, JS thuần`|Tập trung vào kiến thức web cơ bản, giảm sự phức tạp của framework hiện đại.|
|**Quản lý Phiên bản**|`Git / GitHub`|Tiêu chuẩn ngành, sử dụng quy trình **Pull Request** bắt buộc.|
|**Chất lượng Mã nguồn**|`Black` (Formatter) & `Flake8` (Linter)|Tự động thực thi phong cách viết mã chuyên nghiệp và nhất quán.|
|**Triển khai**|`PythonAnywhere / Render`|Các gói dịch vụ miễn phí phù hợp cho dự án sinh viên.|

Xuất sang Trang tính

---

## ⚙️ Quy trình Làm việc & Chất lượng

Nhóm áp dụng các nguyên tắc từ phương pháp **Agile** với quy trình làm việc được định nghĩa nghiêm ngặt:

- **Quy trình Feature Branching:** Mọi tính năng mới đều được phát triển trên một nhánh riêng biệt (`feature/...`) và hợp nhất vào nhánh `main` thông qua Pull Request (PR).
    
- **API-First Bắt buộc:** Hợp đồng API (`/api/v1/summarize`) được định nghĩa và thống nhất trước khi triển khai full-stack để cho phép phát triển song song và giảm thiểu rủi ro tích hợp.
    
- **Đánh giá Mã nguồn (Code Review):** Mọi PR phải được **ít nhất hai thành viên khác** trong nhóm xem xét và phê duyệt trước khi hợp nhất.
    
- **Tự động hóa Chất lượng:** Sử dụng **`pre-commit hooks`** để tự động chạy `black` và `flake8` trước khi commit, đảm bảo mã nguồn luôn tuân thủ tiêu chuẩn chất lượng cao.
    

---

## 🧠 Thuật toán Tóm tắt (NLTK Extractive Summarization)

Thuật toán sử dụng thư viện NLTK để thực hiện tóm tắt trích xuất (extractive summarization) dựa trên tần suất từ vựng. Văn bản được tiền xử lý thông qua các bước tách câu, tách từ, loại bỏ dấu câu và stopwords, sau đó chấm điểm từng câu để chọn ra những câu quan trọng nhất.

Input: Văn bản đầu vào do người dùng nhập, giới hạn tối đa 600 ký tự.

Output: Kết quả tóm tắt gồm khoảng 10 câu quan trọng nhất được chọn lọc tự động từ nội dung gốc.


---

## 👥 Thành viên Nhóm & Vai trò "Lead"

Dự án áp dụng mô hình "**Lead**" để đảm bảo sở hữu chung về kiến thức, mỗi Lead chịu trách nhiệm chính về một lĩnh vực nhưng đồng thời hướng dẫn và chia sẻ kiến thức với các thành viên khác.

|Vai trò "Lead"|Trách nhiệm Chính|
|---|---|
|**Backend & API Lead**|Cấu trúc ứng dụng Flask, định tuyến, xử lý request, và định nghĩa hợp đồng API.|
|**NLP & Core Logic Lead**|Triển khai thuật toán tóm tắt (NLTK), tiền xử lý văn bản và logic chấm điểm câu.|
|**Frontend & UI/UX Lead**|Cấu trúc HTML, tạo kiểu bằng CSS, và logic JavaScript để tương tác với API.|
|**DevOps & QA Lead**|Thiết lập kho chứa GitHub, quản lý triển khai, cấu hình công cụ chất lượng mã nguồn (`black`, `flake8`).|

Xuất sang Trang tính

### Danh sách Thành viên

| Tên                  | GitHub Username | Vai trò Chính         |
| -------------------- | --------------- | --------------------- |
| **Nguyễn Duy Khánh** | `[username_1]`  | Backend & API Lead    |
| **Nguyễn Minh Hưng** | `[username_2]`  | NLP & Core Logic Lead |
| **Liêu Minh Khoa**   | `[username_3]`  | Frontend & UI/UX Lead |
| **Phan Lê Nhật Nam** | `NhatNam-cmd`   | DevOps & QA Lead      |

Xuất sang Trang tính

---

## ✅ Định nghĩa "Hoàn thành" (Definition of "Done" - DoD)

Một nhiệm vụ hoặc toàn bộ dự án chỉ được coi là "**Hoàn thành**" khi đáp ứng tất cả các tiêu chí sau:

1. **MVP được triển khai thành công** trên PythonAnywhere hoặc Render và hoạt động đầy đủ, có thể truy cập công khai.
    
2. Toàn bộ mã nguồn được lưu trữ trong kho chứa **GitHub** chung.
    
3. Mã nguồn vượt qua tất cả các kiểm tra của `flake8` (linter) và `black` (formatter) một cách tự động thông qua `pre-commit hooks`.
    
4. Mỗi thành viên trong nhóm đã tự mình tạo, gửi và hợp nhất thành công ít nhất một nhánh tính năng (feature branch) thông qua quy trình **Pull Request**.
    
5. Các chức năng cốt lõi được ghi lại bằng các bình luận, docstrings và một tệp **`README.md`** toàn diện.
    
6. Nhóm đã chuẩn bị và sẵn sàng cho bài thuyết trình cuối kỳ, bao gồm cả việc **demo trực tiếp** ứng dụng đang hoạt động.

---

**Tài liệu tham khảo chính:**

- [The Flask Mega-Tutorial](https://courses.miguelgrinberg.com/p/flask-mega-tutorial)
    
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development)
    
- [Learn Git Branching (Bắt buộc Tuần 1)](https://learngitbranching.js.org/?locale=en_EN)
    
- [Tài liệu NLTK](https://www.geeksforgeeks.org/nlp/text-summarization-in-nlp/)
    
- [Tài liệu Black Code Formatter](https://black.readthedocs.io/en/stable/getting_started.html)
    
- [Tài liệu Flake8 Linter](https://flake8.pycqa.org/)
