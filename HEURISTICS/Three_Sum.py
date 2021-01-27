# =============================== DESAFIO ================================================ 
# Buscar em um conjunto de dados 3 números que se somados retornem um número específico.
# Dados referentes ao Desafio
# numbers = [12, 3, 1, 2, -6, 5, -8, 6]
# target_sum = 0
# resposta = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
# ========================================================================================

# ======== Tempo: O(n^3) | Espaço: O(1) =========
# ================ 3 Loops ======================
def solution(numbers, target_sum):
    resultado = []
    for i in range(len(numbers) - 2):
        elemento_01 = numbers[i]
        for j in range(i +1, len(numbers) - 1):
            elemento_02 = numbers[j]
            for k in range(i +2, len(numbers)):
                elemento_03 = numbers[k]
                if elemento_01 + elemento_02 + elemento_03 == target_sum:
                    resultado.append(sorted([elemento_01, elemento_02, elemento_03]))
    return resultado
# ======== Tempo: O(n^2) | Espaço: O(n) ===============
# ======== 2 Loops utilizando ponteiros ===============
def solution(numbers, target_sum):
    resultado = []
    lista_ordenada = list(sorted(numbers))
    
    for p in range(len(numbers)):
        p_left = p + 1
        p_right = len(numbers) - 1

        while p_left < p_right:
            soma = lista_ordenada[p] + lista_ordenada[p_left] + lista_ordenada[p_right]
            if soma < target_sum:
                p_left += 1
            elif soma > target_sum:
                p_right -= 1
            else:
                resultado.append([lista_ordenada[p], lista_ordenada[p_left], lista_ordenada[p_right]])

                p_left += 1
                p_right -= 1
    return resultado