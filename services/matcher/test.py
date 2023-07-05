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

    # Definir o tamanho fixo das combinações
    tamanho_combinacoes = 2

    # Gerar as combinações
    comb = itertools.combinations(dados_combinacao.values.tolist(), tamanho_combinacoes)

    # Limitar o número de combinações processadas
    max_combinacoes = 10
    count = 0

   # Iterar sobre as combinações
    for combinacao in comb:
        # Extrair informações da combinação atual
        turma1 = combinacao[0]
        turma2 = combinacao[1]

        # Verificar o número de lugares disponíveis nas salas correspondentes às turmas
        sala1 = df_salas[df_salas['Ambiente'] == turma1[2]]
        sala2 = df_salas[df_salas['Ambiente'] == turma2[2]]

        # Verificar se ambas as salas existem e têm lugares suficientes
        if not sala1.empty and not sala2.empty and sala1['Lugares'].values[0] >= turma1[1] and sala2['Lugares'].values[0] >= turma2[1]:
            # Calcular uma métrica para selecionar a melhor sala (por exemplo, soma dos lugares disponíveis)
            metrica_sala1 = sala1['Lugares'].values[0]
            metrica_sala2 = sala2['Lugares'].values[0]

            # Comparar as métricas para determinar a melhor sala
            if metrica_sala1 > metrica_sala2:
                melhor_sala = sala1
                melhor_turma = turma1
            else:
                melhor_sala = sala2
                melhor_turma = turma2

            # Realizar as operações desejadas com a melhor sala e turma aqui
            # ...
            # ...

        # Imprimir a combinação e a sala selecionada
        print(combinacao)
        print("Melhor sala:", melhor_sala)
        print("Melhor turma:", melhor_turma)

        count += 1
        if count >= max_combinacoes:
            break

        #return combinacao

matcher()