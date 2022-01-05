"""
Par ou impar
"""

num = input('Digite um número inteiro: ')

if num.isnumeric():
    if int(num) % 2 == 0:
        print(f'{num} é um número par.')
    else:
        print(f'{num} é um número impar.')
else:
    print(f'{num} não é um número inteiro.')
