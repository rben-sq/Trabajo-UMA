import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
import os

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

nltk.data.path.append(os.environ.get('NLTK_DATA', '/usr/share/nltk_data'))

def tokenize_text(text):
    return sent_tokenize(text)

def pos_tag_text(text):
    words = nltk.tokenize.word_tokenize(text, language='spanish')
    return nltk.pos_tag(words)

from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']
        if action == 'tokenize':
            result = tokenize_text(text)
            return render_template('result.html', result=result, type='token')
        elif action == 'pos':
            try:
                result = pos_tag_text(text)
                return render_template('result.html', result=result, type='pos')
            except LookupError as e:
                print(f"Error durante el proceso de el POST: {e}")
                return "Error en el momento de la devuelta de el resultado. Porfavor revise los logs."
    return render_template('index.html')