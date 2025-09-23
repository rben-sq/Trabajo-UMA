from __future__ import print_function
import nltk
from syntactic_tagger import SyntacticTagger

""" nltk.download('punkt_tab')"""
""" nltk.download('averaged_perceptron_tagger_eng')  """
""" nltk.download('cess_esp') """

def tokenizar(texto:str):
    return nltk.tokenize.word_tokenize(texto, language='spanish') # Tokeniza el texto en español separando por palabras

def tokenizar_frase(texto:str):
    return nltk.tokenize.sent_tokenize(texto, language='spanish') # Tokeniza el texto en español separando por frases

def etiquetar_en(libro: list):
    # Inicializa el etiquetador de Stanford con el modelo en ingles
    tagged = nltk.pos_tag(libro, lang='spa') # Etiqueta el texto en español
    return tagged

def etiquetar(libro):
    # Inicializa el etiquetador de Stanford con el modelo en español
    tagger = SyntacticTagger()
    tagged = tagger.tag_text(libro)
    return tagged

def maquetar(frase:list):
    # Maqueta el texto etiquetado
    for sentence in frase:
            tokens_line, tags_line, lemmas_line = '|', '|', '|'
            for token, tag, lemma in sentence:
                max_length = max([len(token), len(tag), len(lemma)])
                tokens_line += token + (' ' * (max_length - len(token))) + '|'
                tags_line += tag + (' ' * (max_length - len(tag))) + '|'
                lemmas_line += lemma + (' ' * (max_length - len(lemma))) + '|'
            print('-' * len(tokens_line))
            print(tokens_line)
            print(tags_line)
            print(lemmas_line)
            print('-' * len(tokens_line))
            print()

# texto=input("Introduce el texto a tokenizar: ").split() # para palabras
texto=input("Introduce el texto a tokenizar: ") # para frases
print(tokenizar_frase(texto))
print(etiquetar(texto))