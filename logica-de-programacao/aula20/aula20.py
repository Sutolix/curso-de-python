"""
Listas
fatiamento
append, insert, pop, del, clear, extend, min, max
range
"""
arr = ['A', 'B', 'C', 'D', 'E']
l1 = [2, 2, 0, 2, 3]
l2 = [3, 3, 5, 6, 8, 9, 4, 8]
l3 = l1 + l2

print(arr[0:4:2])  # iniciando do index 0 até o 4 de 2 em 2
print(arr[::2])  # de 2 em 2
print(arr[::-1])  # inverte a lista

print(l3)
l1.extend(l2)  # adiciona em l1 os valores de l2
l1.append('d')  # adiciona 'd' no final da lista
l1.insert(0, 'd')  # adiciona 'd' no index passado(0) e move o indice de todos os elementos para frente
print(l1)

l2.pop()  # remove o último elemento
del(l2[1:4])  # remove os itens do index 1 ao 4

print(max(l2))  # retorna o maior valor
print(min(l2))  # retorna o menor valor


l3 = list(range(1, 10))  # range gera um objeto e para transformar em uma lista é prciso usar a função list()
print(l3)
