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

api_url = "http://localhost:3000"

data = {
    'turmas': requests.get(api_url + "/turmas").json(),
    'salas': requests.get(api_url + "/salas").json()
}

# Criar o DataFrame para os dados das turmas
df_turmas = pd.DataFrame(data['turmas'])
print(df_turmas.head(10))
print('='*90)
# Criar o DataFrame para os dados das salas
df_salas = pd.DataFrame(data['salas'])
print(df_salas.head(100))
print('='*90)
df_combinacoes = pd.concat([df_turmas, df_salas], axis=1)
# print(df_combinacoes.head())


# print(df_turmas.columns)
# print(df_salas.columns)

# print('Turmas')
# print(data['turmas'])
# print('='*50)
# print('Salas')
# print(data['salas'])
# print('='*50)