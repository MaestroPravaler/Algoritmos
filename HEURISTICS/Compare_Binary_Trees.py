# =============================== DESAFIO ================================================ 
# Dadas duas árvores binárias, escreva uma função que indique se elas são iguais ou não.
# As duas árvores binárias são consideradas as mesmas se elas forem estruturalmente 
# identicas e os nós estiverem com o mesmo valor.
# ========================================================================================

# =============================== DFS (Deep First Search) ================================

def solution(tree1, tree2):
    # Toda função recursiva devemos saber onde ela deve parar.
    if tree1 is None or tree2 is None:
        if tree1 == tree2:
            return True
        return False
    
    # Quando chamar?
    if tree1.value == tree2.value:
        return solution(tree1.left, tree2.left) and solution(tree1.right, tree2.right)
    
    return False
    
# ============================== BFS (Breadth First Search) ================================

def solution(tree1, tree2):
    queue = [(tree1, tree2)]

    while queue:
        t1,t2 = queue.pop(0)

        if t1 is None or t2 is None:
            if t1 == t2:
                continue
            return False

        if t1.value != t2.value: 
            return False

        queue.append( (t1.left, t2.left) )
        queue.append( (t1.right, t2.right) )
    return True
