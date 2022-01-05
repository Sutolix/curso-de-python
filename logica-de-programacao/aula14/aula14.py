"""
Formatando valores

:s - Strings
:d - Int
:f - Float
:(character) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

num_1 = 1
num_2 = 'num is {num:1^4}' # coloca o número no centro
print(f'{num_1:0>10}') # Indica que o número precisa ter 10 casas e as que faltarem serão preenchidas com 0 a esquerda.
print(f'{num_1:0>10.2f}') # Define as 10 casas mas adiciona duas casa decimais que também contam
print(num_2.format(num=50))

name = 'Otávio Miranda'
print(f'{name:#^50}')

formatted_name = '{:@>20}'.format(name)
print(formatted_name)

l_name = name.ljust(20, '#')
print(l_name)

print(name.lower()) # tudo minusculo
print(name.upper()) # tudo maiusculo
print(name.title()) # capitalize
