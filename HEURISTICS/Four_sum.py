# =============================== DESAFIO ================================================ 
# O Four Sum é uma variação do problema Two Sum e Three Sum, caso você ainda não tenha feito 
# estes exercícios sugiro que vá primeiro neles e depois volte aqui.
# 
# A idéia deste problema é identificar todos os quatro números que quando somados resultem 
# em um valor especificado.
# 
# Exemplos
# Se o array é [7, 6, 4, -1, 1, 2] e o target é 16. Neste caso, seu programa deve retornar:
# 
# [[7, 6, 4, -1], [7, 6, 1, 2]]
# 
# A soma de todos os valores das listas acima será igual a 16.
# =========================================================================================

def solution(numbers, target_sum):
    hash_table = {}
    result = []

    # pointer - Primeiro ponteiro sempre mais a esquerda
    for pointer in range(len(array)):
        # foward_pointer - Segundo ponteiro que apontará para todos os números posteriores
        for foward_pointer in range(pointer + 1, len(array)):
            my_sum = array[pointer] + array[foward_pointer]
            diff = targetSum - my_sum
            if diff in hash_table:
                for hash_sum in hash_table[diff]:
                    result.append(hash_sum + [array[pointer], array[foward_pointer]])

        # Vamos analisar os números anteriores ao pointer para adicionar 
        # ... as somas dos mesmos no hash_table
        for previous_pointer in range(0, pointer):
            my_sum = array[previous_pointer] + array[pointer]
            if my_sum not in hash_table:
                hash_table[my_sum] = []
            hash_table[my_sum].append([array[previous_pointer], array[pointer]])
	return result