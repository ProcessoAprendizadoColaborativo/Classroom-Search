import requests
import itertools
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

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

    melhor_combinacao_por_turma = {}  # Dicionário para armazenar a melhor combinação por turma

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

melhor_combinacao = matcher()

# Imprimir a melhor combinação para cada turma
for turma_id, (turma, sala, score) in melhor_combinacao.items():
    print(f"A melhor combinação encontrada para a turma {turma} é a sala/laboratório {sala}.")
