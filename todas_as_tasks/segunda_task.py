# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

try:
    n = int(input("Informe um número: "))
    if is_fibonacci(n):
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, informe um número inteiro válido.")


