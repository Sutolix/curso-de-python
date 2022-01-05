"""
Split
Join
Enumerate
"""

string = 'a little test, just one'
arr = ['test', 'a', 'ball']

print(string.split(','))

print(','.join(arr))

for index, value in enumerate(arr):
    print(index, value)

n1, n2, n3 = arr
print(n1)
print(n2)
print(n3)
