'''
Dado uma matriz 2D e uma palavra, identifique se esta determinada palavra está dentro da matriz.

A palavra pode ser construída a partir de letras que estão sequenciais em valores adjacentes, 
onde valores adjacentes são aqueles que estão horizontalmente ou verticalmente por perto.

LEMBRE-SE: a mesma letra não pode ser usada duas vezes para construir uma palavra.

board = [
          ['A','B','C','E'],  
          ['S','F','C','S'],    
          ['A','D','E','E']
        ]
Dada a palavra = "ABCCED", retorne true.
Dada a palavra = "SEE", retorne true.
Dada a palavra = "ABCB", retorne false.
'''
class MySolution:
    board = None
    
    def solution(self, board, word):
        self.board = board
        
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # E a primeira posicao da palavra?
                if self.board[x][y] == word[0]:
                    move = (x, y)
                    if self.deep_first_search(move, [move], word, 0):
                        return True
        return False                    
    
    def deep_first_search(self, current_move, visited_paths, expected_word, word_index):
        if word_index + 1 >= len(expected_word):
            return True
        
        x, y = current_move
        possible_moves = [(x + 1, y),
                          (x - 1, y),
                          (x, y + 1),
                          (x, y - 1)]
        board_x_size = len(self.board)
        board_y_size = len(self.board[0])
        
        for move_x, move_y in possible_moves:
            if move_x >= 0 and move_x < board_x_size and move_y >= 0 and move_y < board_y_size:
                
                if self.board[move_x][move_y] == expected_word[word_index + 1]:
                    if (move_x, move_y) not in visited_paths:
                        
                        next_move = (move_x, move_y)
                        if self.deep_first_search(next_move,
                                                  visited_paths + [next_move],
                                                  expected_word,
                                                  word_index + 1):
                            return True
        return False