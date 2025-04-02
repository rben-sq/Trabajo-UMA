from flask import Flask, request, jsonify
import database
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    conn = database.get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
        values = (data['name'], data['description'], data['price'])
        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Producto creado correctamente'})
    return jsonify({'error': 'Error de conexión a la base de datos'})

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = database.get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        conn.close()
        if product:
            return jsonify({'id': product[0], 'name': product[1], 'description': product[2], 'price': float(product[3])})
        else:
            return jsonify({'message': 'Producto no encontrado'})
    return jsonify({'error': 'Error de conexión a la base de datos'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = database.get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Producto eliminado correctamente'})
    return jsonify({'error': 'Error de conexión a la base de datos'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)