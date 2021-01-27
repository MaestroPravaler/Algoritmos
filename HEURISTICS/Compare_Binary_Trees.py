# =============================== DESAFIO ================================================ 
# Dadas duas árvores binárias, escreva uma função que indique se elas são iguais ou não.
# As duas árvores binárias são consideradas as mesmas se elas forem estruturalmente 
# identicas e os nós estiverem com o mesmo valor.
# ========================================================================================

def solution(tree1, tree2):
    # Quando parar?
    if tree1 is None or tree2 is None:
        if tree1 == tree2:
            return True
        return False
    
    # Quando chamar?
    if tree1.value == tree2.value:
        return solution(tree1.left, tree2.left) and solution(tree1.right, tree2.right)
    
    return False