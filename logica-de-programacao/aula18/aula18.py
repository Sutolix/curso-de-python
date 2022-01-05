text = 'o rato roeu a roupa'
new_text = ''
user_letter = input('Defina uma letra para ser maiúscula: ')

size = len(text)
counter = 0

while counter < size:
    letter = text[counter]
    if letter == user_letter:
        nl = letter.upper()
    else:
        nl = letter
    new_text += nl
    counter += 1

print(new_text)
