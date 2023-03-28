palavra = str(input("Qual palavra deseja inverter?:"))

def inverterPalavra(palavra):
  palavra_invertida = ""

  for i in range((len(palavra)-1), -1, -1):
    palavra_invertida += palavra[i]

  return print(palavra_invertida)


inverterPalavra(palavra)