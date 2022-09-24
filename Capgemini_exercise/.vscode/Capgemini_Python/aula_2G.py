print("Bem vindo")

lado1 = int(input("Lado 1 \n"))
lado2 = int(input("Lado 2 \n"))
lado3 = int(input("Lado 3 \n"))

if (lado1 > lado2 + lado3) or (lado2 > lado1 + lado3) or (lado3 > lado1 + lado2):
    print("Não é um triângulo")
elif (lado1 == lado2) and (lado2 == lado3):
    print("Triângulo Equilátero")
elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")