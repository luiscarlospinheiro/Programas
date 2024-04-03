n = 1
par = impar = 0

while n!=0:
    n = int(input('digite numero: '))
    if n % 2 == 0 and n>1:
        par +=1
    elif n %2>0 and n>1:
        impar+=1
print("vc digitou {} numeros pares e {} numeros impares".format(par,impar))