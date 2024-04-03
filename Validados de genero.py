sexo = str(input('Informe seu sexo [M/F]: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Digite o Sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado'.format(sexo))

