"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""
# Recebendo um número inteiro do usuário
numero = int(input("Digite um número: "))

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    print("Resultado = Par")
else:
    print("Resultado: Ímpar")
