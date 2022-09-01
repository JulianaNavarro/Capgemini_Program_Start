# Laço de repetição

idade_Marcelo = 1.20
print(idade_Marcelo)
idade_Joao = 1.05
print(idade_Joao)
idade = 8

while idade_Joao <= idade_Marcelo:
    idade_Marcelo =  idade_Marcelo + 0.05
    idade_Joao = idade_Joao + 0.07
    idade += 1
else:
    print("Ei, Você ultrapassou o Marcelo")
    # print (f"Idade do João é{idade_Joao}")