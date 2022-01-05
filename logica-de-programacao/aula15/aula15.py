"""
Manipulando strings
"""
# há indices negativos e o último item sempre será o -1 porque o 0 já é o primeiro item
text = 'Python'
print(text[2])

new_text = text[2:6]  # fatia a string e o segundo número do indice não entra. retorna 'thon'
new2_text = text[:5]  # fatia a string pengado do primeiro indice até o 4º

print(new_text)
print(new_text[-1])  # Pega o ultimo item
print(new2_text)
print(text[0:4:2])  # pula de 2 em 2 e para o 4º caracter
