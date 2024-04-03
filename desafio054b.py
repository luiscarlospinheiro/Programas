
i = 0
m = 2024 - i
cont = 0
for c in range(1,5):8
        n = int(input('ano nascimento: '))
        i = 2024 - n

        if  i > 18:
            print('maior de idade')
            cont += 1
        else:
            print('menor de idade')
            print('{} pessoas são maiores de idade'.format(cont))


