"""
Saudações de acordo com a hora
"""

hour = input('Quantas horas são? (0 - 23)')
hour_len = len(hour)

if hour.isnumeric() and 0 > hour_len <= 2:
    hour = int(hour)
    if 0 <= hour <= 11:
        print('Bom dia')
    elif 12 <= hour <= 17:
        print('Boa tarde')
    elif 18 <= hour <= 23:
        print('Boa noite')
    else:
        print('Formato inválido')
else:
    print('Hora inválida')
