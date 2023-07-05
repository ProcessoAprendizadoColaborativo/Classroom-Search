import mysql.connector
from itertools import combinations
from sklearn.linear_model import LinearRegression

class Sala:
    def __init__(self, nome, quantidade_lugares, tipo):
        self.nome = nome
        self.quantidade_lugares = quantidade_lugares
        self.tipo = tipo

class Turma:
    def __init__(self, nome, quantidade_alunos, dia_semana, tipo_sala_restricao):
        self.nome = nome
        self.quantidade_alunos = quantidade_alunos
        self.dia_semana = dia_semana
        self.tipo_sala_restricao = tipo_sala_restricao

class Ensalamento:
    def __init__(self):
        # Estabelecer conexão com o banco de dados
        self.cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="ensalamento"
        )

        # Criação do cursor para executar comandos SQL
        self.cursor = self.cnx.cursor()

        # Criar a tabela 'salas' se ela não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS salas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                quantidade_lugares INT,
                tipo VARCHAR(255)
            )
        """)

        # Criar a tabela 'turmas' se ela não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS turmas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                quantidade_alunos INT,
                dia_semana VARCHAR(255),
                tipo_sala_restricao VARCHAR(255)
            )
        """)

    def inserir_sala(self):
        nome_sala = input("Nome da sala: ")
        quantidade_lugares = int(input("Quantidade de lugares da sala: "))
        tipo_sala = input("Tipo da sala (sala ou laboratório): ")
        sala = Sala(nome_sala, quantidade_lugares, tipo_sala)

        # Inserir a sala no banco de dados
        self.cursor.execute("""
            INSERT INTO salas (nome, quantidade_lugares, tipo)
            VALUES (%s, %s, %s)
        """, (sala.nome, sala.quantidade_lugares, sala.tipo))
        self.cnx.commit()

        resposta = input("Sala inserida com sucesso! Deseja inserir mais salas? (s/n): ")
        if resposta.lower() == 's':
            self.inserir_sala()
        else:
            self.inserir_turma()

    def inserir_turma(self):
        nome_turma = input("Nome da turma: ")
        quantidade_alunos = int(input("Quantidade de alunos da turma: "))
        dia_semana = input("Dia da semana em que a turma tem aula: ")
        tipo_sala_restricao = input("Tipo de sala restrito para a turma (sala ou laboratório): ")
        turma = Turma(nome_turma, quantidade_alunos, dia_semana, tipo_sala_restricao)

        # Inserir a turma no banco de dados
        self.cursor.execute("""
            INSERT INTO turmas (nome, quantidade_alunos, dia_semana, tipo_sala_restricao)
            VALUES (%s, %s, %s, %s)
        """, (turma.nome, turma.quantidade_alunos, turma.dia_semana, turma.tipo_sala_restricao))
        self.cnx.commit()

        resposta = input("Turma inserida com sucesso! Deseja inserir mais turmas? (s/n): ")
        if resposta.lower() == 's':
            self.inserir_turma()
        else:
            self.executar_ensalamento()

    def diferenca_quantidade(self, sala, turma):
        return abs(sala.quantidade_lugares - turma.quantidade_alunos)

    def executar_ensalamento(self):
        # Consultar salas e turmas do banco de dados
        salas = self.consultar_salas()
        turmas = self.consultar_turmas()

        # Criar arrays de características e alvos para treinamento
        X = []
        y = []

        for sala in salas:
            for turma in turmas:
                X.append([sala.quantidade_lugares])
                y.append(turma.quantidade_alunos)

        # Treinar o modelo de regressão linear
        model = LinearRegression()
        model.fit(X, y)

        # Limite de diferença entre quantidade de alunos
        limite_diferenca = 5

        # Dicionário para armazenar as combinações válidas de salas e turmas
        comb_salas_turmas = {}

        # Encontrar as combinações válidas de salas e turmas com quantidade aproximada
        for comb in combinations(salas, 2):
            sala1, sala2 = comb
            for turma in turmas:
                diferenca1 = self.diferenca_quantidade(sala1, turma)
                diferenca2 = self.diferenca_quantidade(sala2, turma)
                if diferenca1 <= limite_diferenca and diferenca2 <= limite_diferenca:
                    dia_semana = turma.dia_semana
                    if dia_semana not in comb_salas_turmas:
                        comb_salas_turmas[dia_semana] = []
                    comb_salas_turmas[dia_semana].append((sala1, sala2, turma))

        # Imprimir as combinações válidas de salas e turmas
        if comb_salas_turmas:
            print("\nCombinações válidas de salas e turmas:")
            for dia_semana, combinacoes in comb_salas_turmas.items():
                print(f"Dia da Semana: {dia_semana}")
                for comb in combinacoes:
                    sala1, sala2, turma = comb
                    print(f"Combinação: {sala1.nome} ({sala1.quantidade_lugares} lugares) - {sala2.nome} ({sala2.quantidade_lugares} lugares) - {turma.nome} ({turma.quantidade_alunos} alunos)")
                print("-------------------------")
        else:
            print("Não foram encontradas combinações válidas de salas e turmas.")
            
        resposta = input("Deseja ver todos os registros salvos ? (s/n): ")
        if resposta.lower() == 's':
            self.exibir_registros()
        else:
            return

    def consultar_salas(self):
        # Consultar salas no banco de dados
        self.cursor.execute("SELECT nome, quantidade_lugares, tipo FROM salas")
        salas = []
        for nome, quantidade_lugares, tipo in self.cursor:
            sala = Sala(nome, quantidade_lugares, tipo)
            salas.append(sala)
        return salas

    def consultar_turmas(self):
        # Consultar turmas no banco de dados
        self.cursor.execute("SELECT nome, quantidade_alunos, dia_semana, tipo_sala_restricao FROM turmas")
        turmas = []
        for nome, quantidade_alunos, dia_semana, tipo_sala_restricao in self.cursor:
            turma = Turma(nome, quantidade_alunos, dia_semana, tipo_sala_restricao)
            turmas.append(turma)
        return turmas

    def exibir_registros(self):
        # Exibir registros da tabela 'salas'
        self.cursor.execute("SELECT * FROM salas")
        salas = self.cursor.fetchall()
        print("Registros da tabela 'salas':")
        for sala in salas:
            print(f"ID: {sala[0]}, Nome: {sala[1]}, Quantidade de Lugares: {sala[2]}, Tipo: {sala[3]}")

        # Exibir registros da tabela 'turmas'
        self.cursor.execute("SELECT * FROM turmas")
        turmas = self.cursor.fetchall()
        print("\nRegistros da tabela 'turmas':")
        for turma in turmas:
            print(f"ID: {turma[0]}, Nome: {turma[1]}, Quantidade de Alunos: {turma[2]}, Dia da Semana: {turma[3]}, Tipo de Sala Restrição: {turma[4]}")

# Criar objeto Ensalamento e executar o programa
ensalamento = Ensalamento()
ensalamento.inserir_sala()
