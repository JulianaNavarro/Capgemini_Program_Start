nota_1 = int(input ("Qual a nota 1? \n"))
nota_2 = int(input ("Qual a nota 2? \n"))
nota_3 = int(input ("Qual a nota 3? \n"))
# nota_media = (nota_1 + nota_2 + nota_3) / 3
nota_media = round((nota_1 + nota_2 + nota_3) / 3,1)


if nota_media < 5 :
    print(f"Você reprovou com a média {nota_media}, sinto muito!!!")
elif nota_media <= 7:
    print(f"Você está de recuperação, sua média foi {nota_media} te vejo no exame!")
else:
    print(f"Você passou! Sua média foi {nota_media}. Parabéns!!! ")


