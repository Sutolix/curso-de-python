"""
For in em Python
Iterando com for
Função range(start=0, stop, step=1)
"""

text = 'Python'

for letter in text:
    print(letter)

for n, letter in enumerate(text):
    print(n, letter)

for n in range(2, 10, 2):
    print(n)
