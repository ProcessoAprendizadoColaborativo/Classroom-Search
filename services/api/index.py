import os
import mysql.connector
import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from itertools import combinations
from fastapi.responses import JSONResponse
import json


load_dotenv()

app = FastAPI()

cnx = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    port=os.environ.get("DB_PORT"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS")
)

cursor = cnx.cursor()


# Endpoint para listar todas as salas
@app.get('/salas')
def get_salas():
    cursor.execute("SELECT * FROM salas")
    result = cursor.fetchall()
    salas = []
    for sala in result:
        sala_dict = {
            "id_sala": sala[0],
            "Ambiente": sala[1],
            "Posicao": sala[2]
        }
        salas.append(sala_dict)
    return JSONResponse(content=salas)


# Endpoint para adicionar uma nova sala
@app.post('/criar-salas')
def add_sala(request: Request):
    data = request.json()
    id_sala = data['id_sala']
    ambiente = data['ambiente']
    posicao = data['posicao']
    sql = "INSERT INTO salas (id_sala, ambiente, posicao) VALUES (%s, %s, %s)"
    values = (id_sala, ambiente, posicao)
    cursor.execute(sql, values)
    cnx.commit()
    return JSONResponse(content={"message": "Sala adicionada com sucesso"})


# Endpoint para listar todas as turmas
@app.get('/turmas')
def get_turmas():
    cursor.execute("SELECT * FROM turmas")
    result = cursor.fetchall()
    turmas = []
    for turma in result:
        turma_dict = {
            "id_turma": turma[1],
            "qtd_alunos": turma[2],
            "turno": turma[3],
        }
        turmas.append(turma_dict)
    return JSONResponse(content=turmas)


# Endpoint para adicionar uma nova turma
@app.post('/criar-turmas')
def add_turma(request: Request):
    data = request.json()
    id_turma = data['id_turma']
    qtd_alunos = data['qtd_alunos']
    turno = data['turno']
    disponibilidade = data["disponibilidade"]
    sql = "INSERT INTO turmas (id_turma, qtd_alunos, turno, disponibilidade) VALUES (%s, %s, %s, %s)"
    values = (id_turma, qtd_alunos, turno, disponibilidade)
    cursor.execute(sql, values)
    cnx.commit()
    return JSONResponse(content={"message": "Turma adicionada com sucesso"})


def combinar_salas_turmas(salas, turmas):
    melhores_solucoes = []
    for r in range(1, len(turmas) + 1):
        combinacoes = combinations(turmas, r)
        for combinacao in combinacoes:
            salas_disponiveis = [sala for sala in salas]
            turmas_validas = []
            sala_valida = True
            for turma in combinacao:
                turma_adicionada = False
                for sala in salas_disponiveis:
                    if turma['qtd_alunos'] <= sala['capacidade'] and turma['disponibilidade'] == sala['disponibilidade']:
                        sala['capacidade'] -= turma['qtd_alunos']
                        turmas_validas.append(turma)
                        turma_adicionada = True
                        break
                if not turma_adicionada:
                    sala_valida = False
                    break
            if sala_valida and len(turmas_validas) == len(turmas):
                melhores_solucoes.append((turmas_validas, list(combinacao)))
    return melhores_solucoes


@app.get('/matchs')
def encontrar_melhores_combinacoes():
    salas = get_salas().json()
    turmas = get_turmas().json()
    melhores_combinacoes = combinar_salas_turmas(salas, turmas)
    return JSONResponse(content=json.dumps(melhores_combinacoes, default=str))


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=3000)
