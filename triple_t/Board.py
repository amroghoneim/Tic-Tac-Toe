class Board():
    def __init__(self, dim= 3):
        '''
            init function for Board class
            
            dim: int, length and width dimensions for board
            game_board: list, Data structure to act as game board
        '''
        self.dim = dim
        self.game_board = []
        print("Created Board")
        
    def initialize_board(self):
        '''
            Function to initialize empty dim x dim board
        '''
        self.game_board = [['-']*self.dim for _ in range(self.dim)]
    
    def __repr__(self):

        out = ""
        for i in range(self.dim):
            for j in range(self.dim):
                out = out + self.game_board[i][j]
            out = out + '\n'
        return out