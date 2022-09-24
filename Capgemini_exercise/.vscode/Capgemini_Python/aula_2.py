import string


print("Hello World")
print("Bye World")

# Tipo de variáveis

nome = input ("Informe o seu nome: \n")
sobrenome = input ("Informe o seu sobrenome? \n")
print(f"{nome} {sobrenome}")

numero1 = int(input ("Qual o número 1 ? \n"))
numero2 = int(input ("Qual o número 2 ? \n"))
soma = numero1 + numero2
print(soma)
subtracao = numero1 - numero2
print(subtracao)
multiplicacao = float(numero1 * numero2)
print(multiplicacao)
divisao = float(numero1 / numero2)
print(divisao)

if numero1 > 10:
    print("True")
else:
    print("False")
