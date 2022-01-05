"""
Desempacotamento de listas
"""

arr = ['Luiz', 'João', 'Maria', 'Carlos', 5, 8, 00, 165, 65, 1]

n1, n2, *rest, last = arr
*_, l1, l2, l3 = arr

print(rest, last)
print(l1, l2, l3)
