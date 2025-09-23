import nltk
from flask import Flask, jsonify, request
from flask_cors import CORS
from nltk import word_tokenize
from nltk import StanfordTagger
from nltk import tokenize

app = Flask(__name__)

CORS(app)
@app.route('/tokenize', methods=['POST'])
def tokenizar():
    data = request.get_json(force=True)  # Obtiene los datos enviados en la petición
    
    listatoken=[]
    # tokens = word_tokenize(data['texto'])
    return nltk.tokenize.sent_tokenize(data, language='espanol')

# Modelo de datos para la respuesta
class TokenizedOutput(BaseModel):
    tokens: List[str]


if __name__ == '__main__':
    app.run(debug=True)