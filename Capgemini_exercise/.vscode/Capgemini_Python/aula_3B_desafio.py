#  Programa que imprime a soma de todos os números pares
#  entre dois números quaisquer, incluindo-os.

print ("Welcome!!!")

num1 = int(input('Entre com o valor inicial:\n'))
num2 = int(input('Entre com o valor final:\n'))
soma = 0

while num1 <= num2:
    if num1 % 2 == 0:
        soma = soma + 1
    num1 = num1 + 1
print(f" A soma é {soma}")