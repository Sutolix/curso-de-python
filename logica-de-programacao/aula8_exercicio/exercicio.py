name = 'Luiz'
age = 32
height = 1.80
weight = 80.5
year = 2021
year_of_birth = year - age
imc = weight / height ** 2

print(f'{name} tem {age} anos, {height} de altura e pesa {weight}kg.')
print(f'O IMC de {name} é {imc:.2f}.')
print(f'{name} nasceu em {year_of_birth}.')
