# Define a lista
nums = []

# O laço será executado enquanto o tamanho da
# lista nums for menor que 4

while len(nums) < 4:
    # Pede ao usuário uma entrada e a armazena em uma variável como número inteiro.
    user_input = int(input("Insira um número inteiro: \n"))
    # Se a entrada for um número par, é adicionada à lista
    if user_input % 2 == 0:
        nums.append(user_input)