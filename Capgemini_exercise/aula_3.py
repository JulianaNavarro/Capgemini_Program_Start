# Laço de repetição

altura_Marcelo = 1.20
altura_Joao = 1.05
idade_Joao = 8

# while altura_Joao < altura_Marcelo:

#     if altura_Joao < altura_Marcelo:
#         altura_Marcelo =  altura_Marcelo + 0.05
#         altura_Joao = altura_Joao + 0.07
#         idade_Joao += 1
    #else:
        #print(altura_Joao)
        #print(f"João voê tem {altura_Joao}, com {idade_Joao} anos, finalmente você passou o Marcelo")

while altura_Joao < altura_Marcelo:
    altura_Marcelo = round(altura_Marcelo + 0.05,3)
    altura_Joao = round(altura_Joao + 0.07,3)
    idade_Joao += 1

print(f"João voê tem {altura_Joao}, e com {idade_Joao} anos, finalmente você passou o Marcelo.")
