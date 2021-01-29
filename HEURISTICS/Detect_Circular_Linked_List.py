# =============================== DESAFIO ================================================ 
# Uma Linked List circular é uma lista em que um dos elementos se relacionam diretamente ou 
# indiretamente entre si.
# 
# class Node:
#     def __init__(self, value):
#         self.next = None
#         self.value = value
# 
# A classe linked_list você pode usar a função .head() para pegar o primeiro item dela.
# ========================================================================================

# ======== Tempo: O(n) | Espaço: O(1) =============
# ============= Lista Circular ====================

def solution(linked_list):
    slow_pointer = linked_list.head()
    fast_pointer = slow_pointer
    
    while slow_pointer:
        if slow_pointer.next is None:
            return False
        if fast_pointer.next is None:
            return False
        
        fast_pointer = fast_pointer.next.next # Pula de 2 em 2
            if fast_pointer == slow_pointer:
            return True
        slow_pointer = slow_pointer.next
    return False