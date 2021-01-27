# =============================== DESAFIO ==================================================
# Dada uma árvore binária que nunca estará vazia, busque o caminho que traga a maior soma de 
# valores.
#
# Neste problema, um caminho é definido pela sequencia de nós que pode iniciar a partir de 
# qualquer nó na árvore. O caminho deve conter ao menos um nó e não precisa iniciar a partir 
# do nó-raiz.
# 
# Entrada:
# 
#   1
#  / \
# 2   3
# 
# Resultado: 6
# ===========================================================================================

class Solution:
    result = float("-inf")
    
    def run(self, root):
        self.dfs(root)
        return self.result
    
    def dfs(self, node):
        if node is None:
            return 0

        left_sum = self.dfs(node.left)
        if left_sum < 0:
            left_sum = 0

        right_sum = self.dfs(node.right)
        if right_sum < 0:
            right_sum = 0

        self.result = max(self.result, left_sum + right_sum + node.value)
        return max(left_sum, right_sum) + node.value