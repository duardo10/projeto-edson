from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="clientes"
)

cursor = db.cursor()

@app.route('/api/clientes', methods=['POST'])
def create_client():
    data = request.json
    name = data['name']
    street = data['street']
    number = data['number']
    city = data['city']
    state = data['state']
    zip_code = data['zip']
    debt_end = data['debt_end']

    query = "INSERT INTO cliente (nome, rua, numero, cidade, estado, cep, data_inicio_divida, data_fim_divida) VALUES (%s, %s, %s, %s, %s, %s,%s, %s)"
    values = (name, street, number, city, state, zip_code, debt_end)
    print('inseriu')

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Cliente criado com sucesso"})

@app.route('/api/clientes', methods=['GET'])
def get_clients():
    query = "SELECT * FROM cliente"
    cursor.execute(query)
    result = cursor.fetchall()

    clients = []
    for row in result:
        client = {
            "id": row[0],
            "name": row[1],
            "street": row[2],
            "number": row[3],
            "city": row[4],
            "state": row[5],
            "zip": row[6],
            "debt_end": row[7]
        }
        clients.append(client)

    return jsonify(clients)


if __name__ == '__main__':
    print('inicializando')
    app.run(debug=True)