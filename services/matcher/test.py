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

    # Verificar se as colunas existem nos DataFrames
    colunas_combinacao = ['id_turma', 'qtd_alunos', 'Ambiente', 'Lugares']  # Substitua pelas colunas relevantes
    if not all(col in df_turmas.columns for col in colunas_combinacao) or not all(col in df_salas.columns for col in colunas_combinacao):
        print("Algumas colunas não foram encontradas nos DataFrames.")
        return melhor_combinacao_por_turma

    # Concatenar os dados das turmas e salas em um único DataFrame
    df_combinacoes = pd.concat([df_turmas, df_salas], axis=1)

    # Extrair as colunas relevantes para a geração das combinações
    dados_combinacao = df_combinacoes[colunas_combinacao]

    # Definir o tamanho das combinações
    tamanho_combinacoes = len(colunas_combinacao) // 2

    # Gerar as combinações
    comb = itertools.combinations(dados_combinacao.index, tamanho_combinacoes)

    for combination in comb:
        # Obter os dados da combinação atual
        dados_combinacao_atual = dados_combinacao.loc[list(combination)]

        # Calcular o custo da combinação atual
        cost = dados_combinacao_atual.shape[0]

        # Iterar sobre as turmas
        for turma_id in df_turmas['id_turma'].unique():
            dados_turma = df_turmas[df_turmas['id_turma'] == turma_id]

            # Verificar se a combinação atual atende aos critérios da turma
            if dados_turma[colunas_combinacao].isin(dados_combinacao_atual.values).all(axis=1).any():
                # Atualizar a melhor combinação para a turma se o custo for menor
                if turma_id not in melhor_combinacao_por_turma or cost < melhor_combinacao_por_turma[turma_id][0]:
                    melhor_combinacao_por_turma[turma_id] = (cost, combination)

    return melhor_combinacao_por_turma

resultado = test()
print(resultado)
