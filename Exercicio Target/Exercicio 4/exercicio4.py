faturamento_mensal = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

def porcentual_rep(faturamento_mensal):
    porcentagens = []
    for item in faturamento_mensal:
        total = sum(faturamento_mensal)
        porcentagem = (item * 100) / total
        porcentagem = round(porcentagem,2)
        porcentagens.append(porcentagem)
    return print(f""""As porcentagens de representação de cada estado é:
    SP:{porcentagens[0]} %
    RJ:{porcentagens[1]} %
    MG:{porcentagens[2]} %
    ES:{porcentagens[3]} %
    Outros:{porcentagens[4]} %
    """)
porcentual_rep(faturamento_mensal)