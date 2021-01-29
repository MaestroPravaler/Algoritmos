# =============================== DESAFIO ================================================ 
# Neste desafio você deverá criar uma estrutura de lista linkada com as seguintes funções. 
# Utilize a classe já declarada ao lado para resolver este desafio.
# 
# insert_node_to_tail(node) => Insere um novo elemento após o último nó da lista.
# 
# insert_node_to_head(node) => Insere um novo elemento como o primeiro nó da lista.
# 
# is_empty() => Verifica se a lista está vazia ou não.
# 
# head() => Retorna o primeiro elemento da lista.
# 
# tail() => Retorna o último elemento da lista.
# ==========================================================================================

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self._head = Node(None)

    def insert_node_to_tail(self, node):
        self.tail().next = node

    def insert_node_to_head(self, node):
        if self._head.next:
            head_element = self._head
            node.next, head_element.next = head_element.next, node
        self._head.next = node

    def is_empty(self):
        return self._head.next is None

    def head(self):
        return self._head.next

    def tail(self):
        current = self._head
        while current.next:
            current = current.next
        return current