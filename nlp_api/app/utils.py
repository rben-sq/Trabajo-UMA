import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

def tokenize_text(text):
    return sent_tokenize(text)

def pos_tag_text(text):
    words = word_tokenize(text)
    return pos_tag(words)
