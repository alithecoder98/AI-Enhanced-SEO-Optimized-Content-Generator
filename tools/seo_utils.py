# tools/seo_utils.py

import re
import spacy
from collections import Counter

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=10):
    doc = nlp(text)
    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    most_common = Counter(words).most_common(top_n)
    return [word for word, freq in most_common]

def calculate_keyword_density(text, keyword):
    keyword_count = len(re.findall(rf"\b{re.escape(keyword)}\b", text, re.IGNORECASE))
    word_count = len(text.split())
    return round((keyword_count / word_count) * 100, 2) if word_count else 0
