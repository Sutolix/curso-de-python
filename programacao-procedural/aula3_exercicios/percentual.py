def aumento_percentual(value, percentage):
    p = value * percentage / 100
    return value + p


percent = aumento_percentual(50, 20)
if percent:
    print(percent)
else:
    print('Parametros inválidos')
