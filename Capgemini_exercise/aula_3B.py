# Enquanto / While

number = input("Digite um número: \n")
while number > 0:
    number = number -1
    print(number)

num = 100
cont_pares = 0
while num <= 200:
    if num % 2 == 0:
        cont_pares = cont_pares + 1
    num = num + 1
print(cont_pares)
