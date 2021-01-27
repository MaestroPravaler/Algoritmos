# =============================== DESAFIO ================================================
# Dado um array numbers com valores 0 e 1, nós podemos alterar K valores de 0 para 1.
# Retorne o tamanho do maior subarray contínuo que contém apenas 1.
#
# numbers = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] 
# K = 2
# Saída: 6
# ========================================================================================

# ======== Tempo: O() | Espaço: O() =========
# ============= Deep First Search ===============

def solution(numbers, k):
    left_pointer = 0
    for right_pointer in range(len(numbers)):
        if numbers[right_pointer] == 0:
            k -= 1

        if k < 0:
            if numbers[left_pointer] == 0:
                k += 1
            left_pointer += 1
    return right_pointer - left_pointer + 1