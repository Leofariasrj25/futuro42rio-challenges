# Desafio #4

# pegando o input e convertendo para tipo inteiro
num_tests = int(input())
# Cria uma lista vazia que irá guardar os resultados da comparações
min_list = []

# para cada triplo de números faça
for i in range(num_tests):

    # pegando os números e depois os convertendo para tipo inteiro
    # porque converter para inteiro? pois queremos realizar operação matemática com os números
    num_a, num_b, num_c = input().split(' ')
    num_a = int(num_a)
    num_b = int(num_b)
    num_c = int(num_c)

    # assumimos que o menor número é num_a
    smallest = num_a

    # caso o segundo número seja menor, então ele passa a ser o menor
    if smallest > num_b:
        smallest = num_b

    # caso o terceiro número seja menor, então ele passa a ser o menor
    if smallest > num_c:
        smallest = num_c
    
    # adicionando o menor número a lista de resultados
    min_list.append(smallest)

# imprimindo a lista
# o argumento sep, informa a função print para separar os itens da lista 
# pelo caractere informado. nesse caso: espaço
print(*min_list, sep=" ")

