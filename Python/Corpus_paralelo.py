import nltk
import nltk.translate.gale_church

""" nltk.download('punkt_tab')"""
""" nltk.download('averaged_perceptron_tagger_eng')  """
""" nltk.download('cess_esp') """

def tokenizar_es(texto:str):
    return texto.split(". ") #nltk.tokenize.sent_tokenize(texto, language='spanish')

def tokenizar_en(texto:str):
    return texto.split(". ") #nltk.tokenize.sent_tokenize(texto, language='english')

def ordenar_corpus(nombre_archivo:str):

    # nombre_archivo = nombre_archivo[:-3]

    texto_es=open(f'Python/Corpus_uploads/{nombre_archivo}_es.txt', 'r', encoding='utf-8').read() # para frases
    libro_es= tokenizar_es(texto_es)
    print(libro_es)
    texto_en=open(f'Python/Corpus_uploads/{nombre_archivo}_en.txt', 'r', encoding='utf-8').read() # para frases
    libro_en= tokenizar_en(texto_en)
    print(libro_en)

    longitud_es = []
    longitud_en = []

    for i in range(len(libro_es)):
        palabras=0
        for char in libro_es[i]:
            if char == ' ' or char == '.':
                palabras+=1
        
        print(palabras)
        longitud_es.append(palabras)

    print("")

    for i in range(len(libro_en)):
        palabras=0
        for char in libro_en[i]:
            if char == ' ' or char == '.':
                palabras+=1
        
        print(palabras)
        longitud_en.append(palabras)

    orden = nltk.translate.gale_church.align_blocks( longitud_es, longitud_en)
    print(orden)

    librordenado_en = [] 
    librordenado_es = [] 

    for i in range(len(orden)):
        librordenado_es.append(libro_es[orden[i][0]])
        librordenado_en.append( libro_en[orden[i][1]])

    # Guardar el texto alineado en un archivo
    with open(f'Python/{nombre_archivo}_alineado_es.txt', 'w', encoding='utf-8') as f:
        for i in range(len(librordenado_es)):
            f.write(f"{librordenado_es[i]}\n\n")
    # Guardar el texto alineado en un archivo
    with open(f'Python/{nombre_archivo}_alineado_en.txt', 'w', encoding='utf-8') as f:
        for i in range(len(librordenado_en)):
            f.write(f"{librordenado_en[i]}\n\n")

ordenar_corpus("tiburon")
    

  
