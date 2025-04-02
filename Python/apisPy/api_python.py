from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
@app.route('/api_python', methods=['POST'])
def resumen():
    """
    Endpoint para recibir datos de ingresos y gastos.
    Espera un JSON con una lista de objetos: [{"anio": 2023, "ingreso": 5000, "gasto": 3000}, ...]
    """
    data = request.get_json(force=True)  # Obtiene los datos enviados en la petición

    # Verifica si se proporcionaron datos
    if not data or not isinstance(data, list):
        return jsonify({"error": "Debe enviar una lista de datos en formato JSON."}), 400  

    aniosresumen = []  # Lista donde se guardará el resumen de cada año

    for anio in data:
        # Validación de los campos en cada objeto
        if not all(key in anio for key in ("anio", "ingreso", "gasto")):
            return jsonify({"error": "Cada objeto debe contener 'anio', 'ingreso' y 'gasto'"}), 400

        beneficio = "Si" if anio["ingreso"] > anio["gasto"] else "No"

        aniosresumen.append({
            "anio": anio["anio"],
            "ingreso": anio["ingreso"],
            "gasto": anio["gasto"],
            "beneficio": beneficio
        })

    return jsonify(aniosresumen)

if __name__ == '__main__':
    app.run(debug=True)
