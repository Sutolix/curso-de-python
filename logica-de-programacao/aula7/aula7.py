name = 'Luiz'
age = 30
height = 1.80
is_adult = age > 18
weight = 80
imc = weight / height ** 2

print(f'{name} tem {age} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(name, age, imc))
print('{2} {0} {0} tem {1} anos e seu imc é {2}'.format(name, age, imc))
print('{n} tem {a} anos e seu imc é {i:.2f}'.format(n=name, a=age, i=imc))
