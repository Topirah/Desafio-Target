import json

with open("dados.json",encoding='utf-8') as dados_json:  #Leitura do arquivo json
    dados = json.load(dados_json)

def faturamento_maximo(dados):
    valores = []
    for item in dados:
        valores.append(item["valor"])
    maximo = max(valores)
    return print(f"O valor máximo é {maximo}, dia {valores.index(maximo)+1}")

def faturamento_minimo(dados):
    valores = []
    dias = []
    for item in dados:
        valores.append(item["valor"])
    minimo = min(valores)
    for m, n in enumerate(valores):
        if n == minimo:
            dias.append(m+1)
    return print(f"O valor mínimo {minimo}, dias {dias}")

def media_mensal(dados):
    valores = []
    valores_maiores = []
    for item in dados:
        if item["valor"] > 0:
            valores.append(item["valor"])
    media = sum(valores)/len(valores)
    for item in valores:
        if item > media:
            valores_maiores.append(item)
    num_dias = len(valores_maiores)  
    return print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi {num_dias} dias")
      
faturamento_maximo(dados)
faturamento_minimo(dados)
media_mensal(dados)