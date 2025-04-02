from flask import Flask, jsonify

app = Flask(__name__)

def es_par(numero: int) -> bool:
    if not isinstance(numero, int):
        raise TypeError("Entrada inválida. Debe proporcionar un número entero.")

    return numero % 2 == 0

@app.route('/apiPrueba/<numero>', methods=['GET'])
def api_es_par(numero: str):
    numero_int = int(numero)
    resultado = es_par(numero_int)
    return jsonify({"Numero": numero_int, "Es": "par" if resultado else "impar"})
if __name__ == '__main__':
    app.run(debug=True)
