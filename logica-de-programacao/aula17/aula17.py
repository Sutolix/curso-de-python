"""
while / else
"""

counter = 1
acc = 1

while counter <= 10:
    print(counter, acc)
    if counter > 5:
        break
    acc += counter
    counter += 1
else:  # se houver um break no while o else não será executado
    print('Else end')
print('End')
