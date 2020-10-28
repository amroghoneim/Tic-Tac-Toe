import random
from .Board import Board
from .Player import Player

class Play(Board, Player):
    
    def __init__(self,  choice = 0, winner=None):
        self.winner = winner
        self.choice = choice
        self.player_1 = None
        self.player_2 = None
        self.board = None
#         Player.__init__(self, '.')
        
    def check_win(self, player, i, j):
        
        if i == 0 and j ==0:
            if self.board.game_board[i+1][j+1] == player.state:
                if self.board.game_board[i+2][j+2] == player.state:
                    self.winner = player
            elif self.board.game_board[i+1][j] == player.state:
                if self.board.game_board[i+2][j] == player.state:
                    self.winner = player
            elif self.board.game_board[i][j+1] == player.state:
                if self.board.game_board[i][j+2] == player.state:
                    self.winner = player
                    
        elif i == 0 and j == 2:
             if self.board.game_board[i+1][j-1] == player.state:
                if self.board.game_board[i+2][j-2] == player.state:
                    self.winner = player
             elif self.board.game_board[i+1][j] == player.state:
                if self.board.game_board[i+2][j] == player.state:
                    self.winner = player
             elif self.board.game_board[i][j-1] == player.state:
                if self.board.game_board[i][j-2] == player.state:
                    self.winner = player
                    
        elif i == 2 and j == 0:
             if self.board.game_board[i-1][j+1] == player.state:
                if self.board.game_board[i-2][j+2] == player.state:
                    self.winner = player
             elif self.board.game_board[i-1][j] == player.state:
                if self.board.game_board[i-2][j] == player.state:
                    self.winner = player
             elif self.board.game_board[i][j+1] == player.state:
                if self.board.game_board[i][j+2] == player.state:
                    self.winner = player
                    
        elif i == 2 and j == 2:
             if self.board.game_board[i-1][j-1] == player.state:
                if self.board.game_board[i-2][j-2] == player.state:
                    self.winner = player
             elif self.board.game_board[i-1][j] == player.state:
                if self.board.game_board[i-2][j] == player.state:
                    self.winner = player
             elif self.board.game_board[i][j-1] == player.state:
                if self.board.game_board[i][j-2] == player.state:
                    self.winner = player
                    
        elif i == 0:
            if self.board.game_board[i+1][j] == player.state:
                if self.board.game_board[i+2][j] == player.state:
                    self.winner = player
            elif self.board.game_board[i][j-1] == player.state:
                if self.board.game_board[i][j+1] == player.state:
                    self.winner = player
        elif i == 2:
            if self.board.game_board[i-1][j] == player.state:
                if self.board.game_board[i-2][j] == player.state:
                    self.winner = player
            elif self.board.game_board[i][j-1] == player.state:
                if self.board.game_board[i][j+1] == player.state:
                    self.winner = player
        elif j == 0:
            if self.board.game_board[i][j+1] == player.state:
                if self.board.game_board[i][j+2] == player.state:
                    self.winner = player
            elif self.board.game_board[i-1][j] == player.state:
                if self.board.game_board[i+1][j] == player.state:
                    self.winner = player
        elif j == 2:
            if self.board.game_board[i+1][j] == player.state:
                if self.board.game_board[i-1][j] == player.state:
                    self.winner = player
            elif self.board.game_board[i][j-1] == player.state:
                if self.board.game_board[i][j-2] == player.state:
                    self.winner = player
        else:
            if self.board.game_board[i+1][j+1] == player.state:
                if self.board.game_board[i-1][j-1] == player.state:
                    self.winner = player
            elif self.board.game_board[i-1][j+1] == player.state:
                if self.board.game_board[i+1][j-1] == player.state:
                    self.winner = player
            elif self.board.game_board[i][j+1] == player.state:
                if self.board.game_board[i][j-1] == player.state:
                    self.winner = player
            elif self.board.game_board[i+1][j] == player.state:
                if self.board.game_board[i-1][j] == player.state:
                    self.winner = player
    
    def fill_square(self, player):
        print("choose square to fill (row,column)")
        row = int(input("row (0-2):"))
        column = int(input("column (0-2):"))
        if self.board.game_board[row][column] == '-':
            print("setting square {},{} with value {}".format(row, column, player.state))
            self.board.game_board[row][column] = player.state
            self.check_win(player, row, column)
            
    def game_loop(self, choice):
#         self.initialize_board()
        
        self.choice = choice
        if self.choice == 0:
            self.player_1.turn = True
        else:
            self.player_2.turn = True
        
        print(self.board)
        while self.winner == None:
            if self.player_1.turn == True:
                self.fill_square(self.player_1)
                self.player_1.turn = False
                self.player_2.turn = True
            elif self.player_2.turn == True:
                self.fill_square(self.player_2)
                self.player_2.turn = False
                self.player_1.turn = True
            print(self.board)
                
        print("GAME OVER! {} WINS!".format(self.winner))
                
    def start_game(self):
        print("TIC TAC TOE")
        self.board = Board()
        self.board.initialize_board()
        self.player_1 = Player('X')
        self.player_2 = Player('O')
        choice = random.choice([0, 1])
        if choice == 0:
            print("X starts the game!")
            self.game_loop(choice)
        else:
            print("O starts the game!")
            self.game_loop(choice)
            
        