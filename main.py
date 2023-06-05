import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
app = Flask(__name__)
cnx = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    port=int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS")

)

corsa = cnx.cursor()

# Endpoint para listar todas as salas
@app.route('/salas', methods=['GET'])
def get_salas():
  
    corsa.execute("SELECT * FROM salas")
    result = corsa.fetchall()
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
    sql = "INSERT INTO salas (id_sala, ambiente, posicao) VALUES (%s, %s, %s)"
    values = (id_sala, ambiente, posicao)
    corsa.execute(sql, values)
    corsa.commit()
    return jsonify({"message": "Sala adicionada com sucesso"})


# Endpoint para listar todas as turmas
@app.route('/', methods=['GET'])
def get_turmas():
    corsa.execute("SELECT * FROM turmas")
    result = corsa.fetchall()
    users = []
    for user in result:
        user_dict = {
            "id_turma": user[0],
            "qtd_alunos": user[1],
            "turno": user[2],
            "disponibilidade": user[3]
        }
        users.append(user_dict)
    return jsonify(users)


# Endpoint para adicionar uma nova turma
@app.route('/criar-turmas', methods=['POST'])
def add_turma():
    data = request.json
    id_turma = data['id_turma']
    qtd_alunos = data['qtd_alunos']
    turno = data['turno']
    diponibilidade = data["disponibilidade"]
    sql = "INSERT INTO turmas (id_turma, qtd_alunos, turno, disponibilidade) VALUES (%s, %s, %s, %s)"
    values = (id_turma, qtd_alunos, turno, disponibilidade)
    corsa.execute(sql, values)
    corsa.commit()
    return jsonify({"message": "Turma adicionada com sucesso"})



if __name__ == '__main__':
    app.run()