# SOBRE FOR - até qdo vc sabe onde quer ir

for caractere in ' Daiane Eu Te Amo ':
    print(caractere)

print("\n") # Blank Line

#  Ex com {}:

notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}



#  Ex com listas

computador = ['Processador', 'Teclado', 'Mouse']

for item in computador:
    print(item)

print("\n") # Blank Line

# VALOR DO WHILE - Qdo vc não sabe até onde vai seu looping.

contador = 0

while contador < 6:
    print(f'Valor do contador é {contador}')
    contador += 1


for chave, valor in notas.items():
    print(f"{chave}: {valor}")
    