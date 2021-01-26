# =============================== DESAFIO ================================================ 
# Buscar em um conjunto de dados dois números que se somados retornem um número específico.
# Dados referentes ao Desafio
numbers = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
target_sum = 9
resposta = [-2, 11] #==> -2 + 11 = 9

# ======== Tempo: O(n²) | Espaço: O(1) =============
# ================ Dois Loops ======================
def solution(numbers, target_sum):
    for i in range(len(numbers) - 1):
        first = numbers[i]
        for j in range(i + 1, len(numbers)):
            second = numbers[j]
            if first + second == target_sum:
                return [first, second]
    return []

# ======= Tempo: O(n) | Espaço O(n) ===========
# ========= Utilizando Hash Table =============
def solution(numbers, target_sum):
    calc_numbers = {}
    for n in numbers:
        y = target_sum - n
        if y in calc_numbers:
            return [y, n]
        else:
            calc_numbers[n] = True
    return []

# ====== Tempo: O(n log n) | Espaço: O(1) ======
# ========= Técnica de dois ponteiros ==========
def solution(numbers, target_sum):
    numbers.sort()
    left_pointer = 0
    right_pointer = len(numbers) - 1
    while left_pointer < right_pointer:
        s = numbers[left_pointer] + numbers[right_pointer]
        if s == target_sum:
            return [numbers[left_pointer], numbers[right_pointer]]
        elif s < target_sum:
            left_pointer += 1
        elif s > target_sum:
            right_pointer -= 1
    return []