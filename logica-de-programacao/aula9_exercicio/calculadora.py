"""
Calculador da aula 9
"""
number_1 = int(input('Digite um número: '))
number_2 = int(input('Digite outro número: '))
print()
print('Agora escolha uma operação digitando o número correnpondente.')
operation = input('\n 1: soma \n 2: subtração \n 3: multiplicação \n 4: divisão \n')

result = 0

if operation == '1':
    print(f'O resultado da soma é {number_1 + number_2}')
elif operation == '2':
    print(f'O resultado da subtração é {number_1 - number_2}')
elif operation == '3':
    print(f'O resultado da multiplicação é {number_1 * number_2}')
elif operation == '4':
    print(f'O resultado da divisão é {number_1 / number_2}')
else:
    print('Você não escolheu uma operação válida.')
