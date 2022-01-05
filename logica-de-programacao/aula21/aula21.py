"""
For / Else
"""

arr = ['luiz', 'joão', 'maria']

for item in arr:
    if item.lower().startswith('x'):
        break
else:
    print('Nenhuma palavra iniciada com X encontrada.')
