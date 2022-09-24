# DIV
# no py se usar // ele semprei irá trazer o resultado inteiro, ou seja, arredondo.
#  com uma / ele traz float, ex:

conta = 34//3
print(conta)

conta2 = 34/3
print(conta2)

# MOD (Modulo) em py, o MOD é o % , sendo que ele traz o que sobrou de uma conta, ex:
conta3 =  34 % 3
print(conta3)
# se o número é par ou impar

numero = int(input("Escolha um número?\n"))
if numero % 2 == 0:
    print(f"Seu número escolhido foi {numero}, ele é Par.")
else:
    print(f"Seu número escolhido foi {numero}, ele é Impar.")
