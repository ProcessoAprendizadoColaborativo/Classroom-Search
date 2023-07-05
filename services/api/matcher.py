import requests
import itertools
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def matcher():
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

    # Definir o tamanho das combinações
    tamanho_combinacoes = len(colunas_combinacao) / 2
    tamanho_combinacoes = int(tamanho_combinacoes)


    # Gerar as combinações
    comb = itertools.combinations(dados_combinacao.values.tolist(), tamanho_combinacoes)

    # Iterar sobre as combinações
    for combinacao in comb:
        print(combinacao)
        # Realizar as operações desejadas com cada combinação aqui
    
    return combinacao

matcher()