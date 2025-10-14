# text_preprocessing_nltk.py
# ----------------------------------------
# Script tiền xử lý văn bản (tokenization, stop-word)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Tải dữ liệu cần thiết
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(text: str):
    """
    Tiền xử lý văn bản:
    - Tách câu
    - Tách từ
    - Loại bỏ dấu câu và stopwords
    """
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens_clean = []

    for sent in sentences:
        words = word_tokenize(sent)
        for w in words:
            w_lower = w.lower()
            if w_lower not in stop_words and w_lower not in string.punctuation:
                tokens_clean.append(w_lower)

    return tokens_clean


if __name__ == "__main__":
    sample_text = """
    Natural Language Processing (NLP) is a field of Artificial Intelligence
    that focuses on the interaction between computers and humans through language.
    The goal is to read, decipher, understand, and make sense of human language.
    """

    print("=== Văn bản gốc ===")
    print(sample_text.strip())

    processed = preprocess_text(sample_text)

    print("\n=== Token sau tiền xử lý ===")
    print(processed)
