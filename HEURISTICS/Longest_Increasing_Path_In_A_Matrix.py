# =============================== DESAFIO ================================================
# Dada uma matriz de inteiros, busque o tamanho do maior caminho em que os valores são 
# incrementais.
# 
# Para cada célula, mova-se em quatro diferentes direções: esquerda, direita, para cima e 
# para baixo. Você não poderá se mover diagonalmente ou para fora da matriz!
# 
# Exemplo 1:
# Entrada: nums = 
# [
#     [9, 9, 4],
#     [6, 6, 8],
#     [2, 1, 1]
# ] 
# Saída: 4
# Explicação: O maior caminho em que os valores são incrementais é [1, 2, 6, 9].
# 
# Exemplo 2:
# Entrada: nums = 
# [
#     [3, 4, 5],
#     [3, 2, 6],
#     [2, 2, 1]
# ] 
# Saída: 4
# Explicação: O maior caminho em que os valores são incrementais é [3, 4, 5, 6].
# ========================================================================================

# == Técnicas utilizadas: Deep first Search e Dymanic Programming =========
# ! Criar matriz com os valores zerados do mesmo tamanho da matriz recibida (count_matrix)
# Enumerar cada item da matriz
# Chamar o DFS (Deep First Search)
# Chamar somente se não tiver o número calculado em nosso (count_matrix)
# Retornar o valor do (count_matrix) na posição atual
# Validar a movimentação e chamar ele mesmo se for uma movimentação válida. (para o próximo passo)
# Retornar o valor maior do (count_matrix)

def solution(matriz):
    # Validação da posição na matriz
    def is_valid_position(pos1, pos2, value):
        if pos1 >= 0 and pos1 < vertical_size:
            if pos2 >= 0 and pos2 < horizontal_size:
                return value < matriz[pos1][pos2] # Se for maior ou igual retorna false e não'é uma posição válida.
    # Função para realizar o deep first search
    def dfs(pos1, pos2):
        if count_matrix[pos1][pos2] == 0:
            value = matriz[pos1][pos2]
            # As 4 posições válidas são:
            # (pos1 + 1, pos2) (pos1 - 1, pos2) (pos1, pos2 + 1) (pos1, pos2 - 1)
            max_path = 0 #maior caminho que eu tenho
            for next_pos1, next_pos2 in [(pos1 + 1, pos2), (pos1 - 1, pos2), (pos1, pos2 + 1), (pos1, pos2 - 1)]:
                if is_valid_position(next_pos1, next_pos2, value):
                    max_path = max(max_path, dfs(next_pos1, next_pos2))
            count_matrix[pos1][pos2] = 1 + max_path
        return count_matrix[pos1][pos2]

    result = 0
    if matriz and matriz[0]:
        # ! Peguei os valores da matriz de origem
        vertical_size, horizontal_size = len(matriz), len(matriz[0])
        # ! Criação da Matriz de comparação
        count_matrix = [[0] * horizontal_size for i in range(vertical_size)]
        # Supondo: vertical_size e horizontal size = 3
        # Criei um array de zeros, [0] * 3 [0, 0, 0] -> [[0, 0, 0],[0, 0, 0],[0, 0, 0]] 3 vezes
        for pos1 in range(vertical_size):
            for pos2 in range(horizontal_size):
                result = max(result, dfs(pos1, pos2))
    
    return result