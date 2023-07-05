import os
import json
import uvicorn
import requests
import itertools
import numpy as np
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
from itertools import combinations
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from fastapi.middleware.cors import CORSMiddleware
from sklearn.model_selection import train_test_split



load_dotenv()

cnx = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    port=os.environ.get("DB_PORT"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS")
)

def test():

    melhor_combinacao_por_turma = {}

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

    # Fazer a concatenação dos dataframes usando as colunas correspondentes
    df_combinado = pd.merge(df_turmas, df_salas, left_on='id_turma', right_on='Ambiente', how='outer')
    
    # Realizar a combinação entre turmas e salas
    melhor_combinacao = None
    melhor_pontuacao = 0

    # Verificar se a junção resultou em algum resultado
    if not df_combinado.empty:
        # Extrair as colunas relevantes para a geração das combinações
        colunas_combinacao = ['id_turma', 'qtd_alunos', 'Ambiente', 'Lugares']

        # Filtrar as colunas relevantes do dataframe combinado
        dados_combinacao = df_combinado[colunas_combinacao]

        # Definir o tamanho das combinações
        tamanho_combinacoes = len(colunas_combinacao) // 2

        # Gerar as combinações
        comb = itertools.combinations(dados_combinacao.values.tolist(), tamanho_combinacoes)
        
        # Iterar sobre as turmas
        for turma in data['turmas']:
            # Filtrar os dados de combinação apenas para a turma atual
            turma_id = turma['id_turma']
            alunos = turma['qtd_alunos']
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
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Treinar o classificador DecisionTree
                clf = DecisionTreeClassifier()
                clf.fit(X_train, y_train)

                # Avaliar o classificador
                score = clf.score(X_test, y_test)

                # Verificar se essa combinação é a melhor até o momento para a turma atual
                if score > melhor_score:
                    melhor_combinacao = combinacao
                    melhor_score = score


    for index, row in df_turmas.iterrows():
        turma = row['Turma']
        quantidade_alunos = row['Quantidade de Alunos']
    for index, row in df_salas.iterrows():
        sala = row['Sala']
        capacidade = row['Capacidade']
        # Calcular a pontuação da combinação
        pontuacao = calcular_pontuacao(turma, sala)
        
        if pontuacao > melhor_pontuacao and quantidade_alunos <= capacidade:
            melhor_combinacao = (turma, sala)
            melhor_pontuacao = pontuacao

    print("Melhor combinação:", melhor_combinacao, "com pontuação:", melhor_pontuacao)

    # Verificar se foi encontrada alguma combinação para a turma atual
    if melhor_combinacao is not None:
        turma_id = melhor_combinacao[0][0]  # ID da turma
        sala = melhor_combinacao[0][0]  # Sala/laboratório

        # Armazenar a melhor combinação para a turma atual
        melhor_combinacao_por_turma[turma_id] = (turma_id, sala, melhor_score)
        print(f"Turma: {turma_id}, com a melhor combinação: {sala}, Score: {melhor_score}")
    else:
        print("Nenhuma combinação encontrada para a turma atual")

    return melhor_combinacao_por_turma

test()