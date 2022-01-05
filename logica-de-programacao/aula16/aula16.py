"""
while - repetição
"""

n = 1
while n <= 10:
    if n == 5:
        n += 1
        continue
    if n == 10:
        break
    print(n)
    n += 1
print('End')

x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
print('End')

while True:
    print()
    exit_calc = input('Deseja sair? [s]im ou [n]ão ')
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operator = input('Digite um operador: ')

    if exit_calc == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')
