def checarFibonacci(i):
  termo1 = 0
  termo2 = 1
  num = 0
  while num < i:
    num = termo1 + termo2
    termo1 = termo2
    termo2 = num
    if num == i:
      return print(f'{i} pertence a sequencia de Fibonacci')
  print(f'{i} não pertence a sequencia de Fibonacci')

numero = int(input("Informe o numero que sera analisado na sequencia de fibonacci:"))

checarFibonacci(numero)