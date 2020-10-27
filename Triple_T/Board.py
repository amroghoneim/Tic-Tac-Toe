class Board():
    def __init__(self, length= 3, width = 3):
        self.length = length
        self.width = width 
        self.board = []
        
    def initialize_board(self):
        self.board = [['-']*self.length]*self.width
    
    def __repr__(self):
        out = ""
        for i in range(self.length):
            for j in range(self.width):
                out = out + self.board[i][j]
            out = out + '\n'
        return out