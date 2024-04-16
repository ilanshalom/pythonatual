def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    tax = float(valor_hora)
    if horas <= 40:
     salario=horas*tax
    else:
        h_excd = horas - 40
        salario = 40*tax+(h_excd*(1.5*tax))
        return salario
str_horas = input('digite as horas: ')
str_tax = input('digite o valor-hora: ')
total_salario = calcular_pagamento(str_horas,str_tax)
print('O valor de seus rendimentos é R$ ', total_salario)