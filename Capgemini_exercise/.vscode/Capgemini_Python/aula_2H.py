# potencia (altura x altura ( ** )) -  IMC

altura = float(input("Qual a sua altura por favor? \n"))
peso = int(input("Informe seu peso por gentileza \n"))
# # imc = peso / (altura * altura)
imc = round(peso / (altura ** 2 ),2)
# print(imc)

if imc < 19:
    print(f"Você está abaixo do peso, o seu imc é {imc}.")
elif imc <24:
    print(f"Você está com o peso ideal, o seu imc é {imc}.") 
else:
    print(f"Você está acima do peso, o seu imc é {imc}")




