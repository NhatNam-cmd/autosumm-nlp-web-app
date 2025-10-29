# summarizer.py
# ----------------------------------------
# Lớp Summarizer - Thuật toán tóm tắt trích xuất (extractive summarization)

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from text_preprocessing_nltk import preprocess_text

nltk.download("punkt")


class Summarizer:
    """
    Lớp Summarizer thực hiện tóm tắt văn bản bằng phương pháp trích xuất.
    Quy trình:
        1. Tiền xử lý văn bản
        2. Tính tần suất từ
        3. Chấm điểm các câu
        4. Chọn ra n câu quan trọng nhất làm bản tóm tắt
    """

    def __init__(self):
        pass

    def score_sentences(self, text: str):
        """Tính điểm cho từng câu dựa trên tần suất xuất hiện của từ"""
        sentences = sent_tokenize(text)
        tokens_clean = preprocess_text(text)

        # Tạo bảng tần suất từ
        freq_table = {}
        for word in tokens_clean:
            freq_table[word] = freq_table.get(word, 0) + 1

        # Chấm điểm cho từng câu
        sentence_scores = {}
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            sentence_scores[sentence] = sum(freq_table.get(w, 0) for w in words)

        return sentence_scores

    def summarize(self, text: str, n: int = 3):
        """Trả về bản tóm tắt gồm n câu có điểm cao nhất"""
        sentence_scores = self.score_sentences(text)
        # Lấy top n câu có điểm cao nhất
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]

        # Giữ đúng thứ tự xuất hiện gốc
        sentences_ordered = sent_tokenize(text)
        summary = [s for s in sentences_ordered if s in top_sentences]

        return summary

