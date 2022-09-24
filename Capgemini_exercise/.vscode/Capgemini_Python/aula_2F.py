# Tabela verdade

# AND // E
# SIM E NÃO = NÃO
# NÃO E SIM = NÃO
# SIM E SIM = SIM
# NÃO E NÃO = NÃO
numero1 = int(input("Qual número 1? \n"))
numero2 = int(input("Qual número 2? \n"))

if numero1 == 10 and numero2 == 20:
    print("Fazer algo")
else:
    print("Não fazer nada.")

# OR // OU
# SIM E NÃO = SIM
# NÃO E SIM = SIM
# SIM E SIM = SIM
# NÃO E NÃO = NÃO
numero1 = int(input("Qual número 1? \n"))
numero2 = int(input("Qual número 2? \n"))

if numero1 == 10 or numero2 == 20:
    print("Fazer algo")
else:
    print("Não fazer nada.")