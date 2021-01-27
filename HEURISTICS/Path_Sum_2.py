# =============================== DESAFIO ================================================
# Dada uma árvore binária e uma soma, busque todos os caminhos que tenham a somatória 
# especificada.
#
# Importante: Um caminho válido é aquele que vá para a raiz até um nó sem nenhum filho
# 
# Exemplo:
# Data a árvore binária abaixo e a soma 22,
# 
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Deverá retornar:
# 
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# Estes são os caminhos que a soma total é igual a 22.
# =========================================================================================

class Solution:
    def run(self, root, expected_sum):
        result = []
        if root:
            self.dfs(root, [], 0, expected_sum, result)        
        return result
    
    def dfs(self, node, current_path, current_sum, expected_sum, result):
        if node is None:
            return
        current_sum += node.value        
        node_without_leaf = node.left is None and node.right is None
        if node_without_leaf and current_sum == expected_sum:
            result += [current_path + [node.value]]
            return
        
        self.dfs(node.left, current_path + [node.value], current_sum, expected_sum, result)
        self.dfs(node.right, current_path + [node.value], current_sum, expected_sum, result)