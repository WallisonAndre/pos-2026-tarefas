import requests
from getpass import getpass

user = input("Digite sua matrícula: ")
password = getpass("Digite sua senha: ")
ano = input("Ano: ")
periodo = input("Período: ")

data = {"username": user, "password": password}
response = requests.post("https://suap.ifrn.edu.br/api/token/pair", json=data)

token = response.json()["access"]
headers = {"Authorization": f"Bearer {token}"}

# Busca o boletim
url = f"https://suap.ifrn.edu.br/api/ensino/meu-boletim/{ano}/{periodo}/"
dados = requests.get(url, headers=headers).json()

if isinstance(dados, dict):
    dados = dados.get("results", [])

print("\nNOTAS:")

for d in dados:
    nome = d.get("disciplina")
    n1 = d.get("nota_etapa_1")
    n2 = d.get("nota_etapa_2")
    n3 = d.get("nota_etapa_3")
    n4 = d.get("nota_etapa_4")
    media = d.get("media_final_disciplina")
    situacao = d.get("situacao")
    
    print(f"{nome} -> N1: {n1}, N2: {n2}, N3: {n3}, N4: {n4} | Média: {media} | {situacao}")