secret = 'perfume'
typed = []
attempts = 3

while True:

    if attempts == 0:
        print('Você perdeu :(')
        break

    letter = input('Digite uma letra: ')
    if len(letter) > 1:
        print('Por favor digite apenas uma letra.')
        continue

    if letter in secret:
        print(f'Ok, "{letter}" existe na palavra secreta')
        typed.append(letter)
    else:
        print(f'Incorreto, "{letter}" NÃO EXISTE na palavra secreta')
        attempts -= 1
        print(f'Vocẽ ainda tem {attempts} chances.')
        continue

    temp = ''
    for secret_letter in secret:
        if secret_letter in typed:
            temp += secret_letter
        else:
            temp += '*'
    print(temp)

    if temp == secret:
        print(f'Você acertou! A palavra secreta era "{secret}".')
        break
