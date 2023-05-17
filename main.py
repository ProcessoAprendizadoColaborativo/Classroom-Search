import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify, request
load_dotenv()

app = Flask(__name__)

cnx = mysql.connector.connect(
    host= os.environ.get("DB_HOST"),
    port= int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER"),
    database=os.environ.get("DB_NAME")
)

cursor = cnx.cursor()

# Endpoint para listar todas as salas
@app.route('/', methods=['GET'])
def get_salas():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM salas")
    result = cursor.fetchall()
    users = []
    for user in result:
        user_dict = {
            "id_sala": user[0],
            "Ambiente": user[1],
            "Posicao": user[2]
        }
        users.append(user_dict)
    return jsonify(users)

# Endpoint para adicionar uma nova sala
@app.route('/criar-salas', methods=['POST'])
def add_sala():
    data = request.json
    id_sala = data['id_sala']
    ambiente = data['ambiente']
    posicao = data['posicao']
    cursor = mydb.cursor()
    sql = "INSERT INTO users (id_sala, ambiente, posicao) VALUES (%s, %s, %s)"
    values = (id_sala, ambiente, posicao)
    cursor.execute(sql, values)
    mydb.commit()
    return jsonify({"message": "Sala adicionada com sucesso"})

if __name__ == '__main__':
    app.run()
