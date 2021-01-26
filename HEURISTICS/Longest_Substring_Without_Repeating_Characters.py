# Data uma string, retorne o tamanho da maior substring que não tenha nenhum caracter repetido.

# Entrada: abcabcbb Saida: 3
# Resposta: O valor encontrado é "abc", que tem o tamanho 3.

# ======== Tempo: O(n) | Espaço: O(n) =========
# ================ hash Table ======================

def solution(s):
    result = 0
    
    for first_pointer in range(len(s)):
        hash_table = {s[first_pointer]: True}
        second_pointer = first_pointer
        
        while True:
            second_pointer += 1
            if second_pointer >= len(s) or s[second_pointer] in hash_table:
                result = max(len(hash_table.keys()), result)
                break
                
            hash_table[s[second_pointer]] = True
            
    return result