# =============================== DESAFIO ================================================
# Dada uma árvore binária, encontre a menor profundidade da mesma.
# A profundidade mínima é o número de nós que formam o menor caminho entre a raiz e o nó 
# sem nenhum filho da árvore.
#
# Nota: Um nó considerado sem nenhum filho é aquele em que o left e o right são nulos, 
# ou seja, não tem nenhum filho.
# Exemplo:
# Dada a árvore binária [3, 9, 20, None, None, 15, 7],
# 
#   3
#  / \
# 9  20
#   /  \
#  15   7
# O resultado é 2 pois o menor caminho passa pelos números 3 e 9.
# =========================================================================================

def solution(root):
  # Sempre verifique o parâmetro que vc está recebendo
  if root:
    queue = [(root, 1)]
    while queue:
      node, level = queue.pop(0)
      if node.left is None and node.right is None:
        return level

      level += 1 # Caso tiver filhos tem de incrementar o level
      if node.left:
        queue.append( (node.left, level) )  
      if node.right:
        queue.append( (node.right, level) )

  return 0
