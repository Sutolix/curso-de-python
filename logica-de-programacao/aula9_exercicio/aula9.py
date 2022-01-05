"""
Entrada de dados
"""

name = input("Qual o seu nome? ")
age = input("Qual sua idade? ")

year_of_birth = 2021 - int(age)

print(f'{name} tem {age} anos. '
      f'{name} nasceu em {year_of_birth}')
