import itertools
import requests

dados = ['A', 'B', 'C', 'D']
# Fazer a solicitação à API para obter os dados do banco de dados
# response = requests.get('http://localhost:3000/salas')
# dados = response.json()


# Definindo o tamanho das combinações
tamanho = len(dados)/2 

tamanho_combinacoes = tamanho 

tamanho_combinacoes = int(tamanho_combinacoes) 

# Gerando as combinações
comb = itertools.combinations(dados, tamanho_combinacoes)

# Iterando sobre as combinações
for combinacao in comb:
    print(combinacao)
    # Faça as operações desejadas com cada combinação aqui
