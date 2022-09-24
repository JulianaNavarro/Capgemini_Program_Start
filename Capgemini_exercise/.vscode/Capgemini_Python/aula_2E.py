print("Avaliador de Multa")

velocidade = int(input("Qual a velocidade que o automóvel passou? \n"))
velocidade_leve = 50 * 1.1
velocidade_media = 70 * 1.1
velocidade_grave = 90 * 1.1
velocidade_gravisima = 110 * 1.1

if velocidade <= velocidade_leve:
    print(" Você está isento de multa ")
elif velocidade <= velocidade_media:
    print("Você receberá uma multa e 3 pontos na carteira ")
elif velocidade <= velocidade_grave:
    print("Eitaaa heim! Você receberá uma multa e 5 pontos na carteira ")
else:
    print("MINHA NOSSA!!! Você receberá uma multa e 7 pontos na carteira ")