"""
Valida CPF
"""
inserted_cpf = 0
while len(str(inserted_cpf)) != 11:
    inserted_cpf = input('Digite seu cpf: ')
    if len(inserted_cpf) == 0:
        print('Por favor digite 11 números.')


def validate(val):
    ref = 11 - (val % 11)
    if ref > 9:
        return str(0)
    else:
        return str(ref)


main_numbers = inserted_cpf[:-2]

first_sum = 0
for i, r in enumerate(range(10, 1, -1)):
    first_sum += int(main_numbers[i]) * r
first_n = validate(first_sum)

second_sum = 0
for i, r in enumerate(range(11, 1, -1)):
    if i == 9:
        second_sum += int(first_n) * r
    else:
        second_sum += int(main_numbers[i]) * r
second_n = validate(second_sum)

new_cpf = main_numbers + first_n + second_n
if inserted_cpf == new_cpf:
    print('CPF válido')
else:
    print('CPF inválido')
