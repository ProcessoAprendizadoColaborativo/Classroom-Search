import os
import json
import uvicorn
import mysql.connector
from matcher import matcher
from dotenv import load_dotenv
from itertools import combinations
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


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

# Configurar os domínios permitidos para solicitações CORS
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

# Adicionar o middleware CORS ao aplicativo FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            "Lugares": sala[3]
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
    lugares = data['lugares']
    sql = "INSERT INTO salas (id_sala, ambiente, posicao, lugares) VALUES (%s, %s, %s)"
    values = (id_sala, ambiente, posicao, lugares)
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


@app.route('/combine', methods=['POST'])
async def matcher():
    # Configurar a URL da API
    api_url = "http://localhost:3000"

    # Fazer uma solicitação GET para obter os dados das turmas e salas/laboratórios
    data = {
        'turmas': requests.get(api_url + "/turmas").json(),
        'salas': requests.get(api_url + "/salas").json()
    }

    # Criar o DataFrame para os dados das turmas
    df_turmas = pd.DataFrame(data['turmas'])

    # Criar o DataFrame para os dados das salas
    df_salas = pd.DataFrame(data['salas'])

    # Verificar se a coluna "Ambiente" está presente nos DataFrames df_turmas e df_salas
    coluna_ambiente_presente = "Ambiente" in df_salas.columns

    # Concatenar os dados das turmas e salas em um único DataFrame
    df_combinacoes = pd.concat([df_turmas, df_salas], axis=1)

    # Extrair as colunas relevantes para a geração das combinações
    colunas_combinacao = ['id_turma', 'qtd_alunos', 'Ambiente', 'Lugares']  # Substitua pelas colunas relevantes
    if coluna_ambiente_presente:
        colunas_combinacao.append("Ambiente")

    dados_combinacao = df_combinacoes[colunas_combinacao]

    melhor_combinacao_por_turma = {}  # Dicionário para armazenar a melhor combinação wpor turma

    # Iterar sobre as turmas
    for turma in data['turmas']:
        # Filtrar os dados de combinação apenas para a turma atual
        turma_id = turma['id_turma']
        dados_turma = dados_combinacao[dados_combinacao['id_turma'] == turma_id]

        # Definir o tamanho das combinações
        tamanho_combinacoes = len(colunas_combinacao) // 2

        # Gerar as combinações
        comb = itertools.combinations(dados_turma.values.tolist(), tamanho_combinacoes)

        # Variáveis para armazenar a melhor combinação e o melhor score da turma atual
        melhor_combinacao = None
        melhor_score = 0

        # Iterar sobre as combinações
        for combinacao in comb:
            turmas = [list(c[:-1]) for c in combinacao]  # Extrair apenas as colunas das turmas, excluindo o ambiente
            salas = [c[-1] for c in combinacao]  # Obter a coluna de salas/laboratórios

            if len(turmas) == len(salas):  # Verificar se o número de amostras é consistente
                # Codificar as variáveis categóricas
                label_encoder = LabelEncoder()
                turmas_encoded = [label_encoder.fit_transform(turma) for turma in zip(*turmas)]
                salas_encoded = label_encoder.fit_transform(salas)

                # Converter as listas codificadas em um array NumPy
                X = np.array(turmas_encoded).T
                y = np.array(salas_encoded)

                # Dividir os dados em treino e teste
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=50)

                # Treinar o classificador DecisionTree
                clf = DecisionTreeClassifier()
                clf.fit(X_train, y_train)

                # Avaliar o classificador
                score = clf.score(X_test, y_test)

                # Verificar se essa combinação é a melhor até o momento para a turma atual
                if score > melhor_score:
                    melhor_combinacao = combinacao
                    melhor_score = score

        # Verificar se foi encontrada alguma combinação para a turma atual
        if melhor_combinacao is not None:
            turma_id = melhor_combinacao[0][0]  # ID da turma
            sala = melhor_combinacao[-1][-1]  # Sala/laboratório

            # Armazenar a melhor combinação para a turma atual
            melhor_combinacao_por_turma[turma_id] = (turma_id, sala, melhor_score)

    return melhor_combinacao_por_turma


# Plano B
## def combinar_salas_turmas(salas, turmas):
#     melhores_solucoes = []
#     for r in range(1, len(turmas) + 1):
#         combinacoes = combinations(turmas, r)
#         for combinacao in combinacoes:
#             salas_disponiveis = [sala for sala in salas]
#             turmas_validas = []
#             sala_valida = True
#             for turma in combinacao:
#                 turma_adicionada = False
#                 for sala in salas_disponiveis:
#                     if turma['qtd_alunos'] <= sala['capacidade'] and turma['disponibilidade'] == sala['disponibilidade']:
#                         sala['capacidade'] -= turma['qtd_alunos']
#                         turmas_validas.append(turma)
#                         turma_adicionada = True
#                         break
#                 if not turma_adicionada:
#                     sala_valida = False
#                     break
#             if sala_valida and len(turmas_validas) == len(turmas):
#                 melhores_solucoes.append((turmas_validas, list(combinacao)))
#     return melhores_solucoes


## @app.get('/matchs')
## def encontrar_melhores_combinacoes():
#     salas = get_salas().json()
#     turmas = get_turmas().json()
#     melhores_combinacoes = combinar_salas_turmas(salas, turmas)
#     return JSONResponse(content=json.dumps(melhores_combinacoes, default=str))


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=3000)
