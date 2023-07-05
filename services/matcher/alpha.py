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

    # Concatenar os dados das turmas e salas em um único DataFrame
    df_combinacoes = pd.concat([df_turmas, df_salas], axis=1)

    # Extrair as colunas relevantes para a geração das combinações
    colunas_combinacao = df_combinacoes.columns

    dados_combinacao = df_combinacoes[colunas_combinacao]

    # Definir o tamanho das combinações
    tamanho_combinacoes = len(colunas_combinacao) // 2

    # Gerar as combinações
    comb = itertools.combinations(dados_combinacao.values.tolist(), tamanho_combinacoes)

    # Dicionários para armazenar os estados anteriores e os custos acumulados
    previous_state = {}
    cost_so_far = {}
    combinations_list = []

    # Inicializar o estado atual e o custo acumulado para a combinação inicial
    initial_combination = next(comb)
    current_state = initial_combination
    cost_so_far[0] = 0
    combinations_list.append(initial_combination)

    combination_index = 1
    max_combinations = 100

    while comb and combination_index < max_combinations:
        combination = next(comb, None)
        if not combination:
            break

        previous_state[combination_index] = current_state
        current_state = combination

        # Calcular o novo custo acumulado
        def calculate_cost(combination):
            # Substitua esta lógica pela sua própria implementação para calcular o custo da combinação
            cost = len(combination)
            return cost

        new_cost = calculate_cost(current_state)

        # Verificar se a combinação atual já foi visitada ou se o novo custo é menor que o custo anterior
        if combination_index not in cost_so_far or new_cost < cost_so_far[combination_index]:
            cost_so_far[combination_index] = new_cost
            combinations_list.append(current_state)

        combination_index += 1

    melhor_combinacao_por_turma = {
        turma_id: combination
        for turma_id, combination in enumerate(combinations_list, start=1)
    }

    return melhor_combinacao_por_turma

def melhor_combinacao_salas_turmas(melhor_combinacao_por_turma):
    mensagens = []
    for chave, valor in melhor_combinacao_por_turma.items():
        for combinacao in valor:
            for sala, turma in zip(combinacao[:len(combinacao)//2], combinacao[len(combinacao)//2:]):
                id_sala, ambiente, lugar = sala[0], sala[1], sala[2]
                id_turma, qtd_alunos, turno = turma[0], turma[1], turma[2]
                
                mensagem = f"A Sala: {id_sala}, com: {lugar} lugares, servirá bem para a turma {id_turma}, com {qtd_alunos} alunos no turno {turno}"
                mensagens.append(mensagem)
    
    return mensagens



# def melhor_combinacao_salas_turmas(melhor_combinacao_por_turma):
#     mensagens = []
#     for chave, valor in melhor_combinacao_por_turma.items():
#         for sala, turma in valor:
#             id_sala, ambiente, lugar = sala[4], sala[1], sala[5]
#             id_turma, qtd_alunos, turno = turma[0], turma[1], turma[2]
        
#         mensagem = f"A Sala: {id_sala}, com: {lugar} lugares, servirá bem para a turma {id_turma}, com {qtd_alunos} alunos no turno {turno}"
#         mensagens.append(mensagem)
    
#     return mensagens


# Exemplo de uso
resultado = test()
melhores_combinacoes = melhor_combinacao_salas_turmas(resultado)
for mensagem in melhores_combinacoes:
    print(mensagem)
