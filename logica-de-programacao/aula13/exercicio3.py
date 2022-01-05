
name = input('Digite seu nome: ')
name_len = len(name)

if name_len <= 4:
    print('Seu nome é curto')
elif 5 >= name_len <= 6:
    print('Seu nome é normal')
elif name_len > 6:
    print('Seu nome é muito grande')
