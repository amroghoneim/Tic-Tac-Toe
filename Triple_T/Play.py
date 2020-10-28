import random
from .Board import Board
from .Player import Player

class Play(Board, Player):
    
    def __init__(self, winner=None, board, player_1, player_2, choice = 0):
        self.winner = winner
        self.board = Board.__init__()
        self.board.initialize_board()
        self.player_1 = Player.__init__('X')
        self.player_2 = Player.__init__('O')
        self.choice = choice
    
    def check_win(self, player, i, j):
        
        if i == 0 and j ==0:
            if self.board.board[i+1][j+1] == player.state:
                if self.board.board[i+2][j+2] == player.state:
                    self.winner = player
            elif self.board.board[i+1][j] == player.state:
                if self.board.board[i+2][j] == player.state:
                    self.winner = player
            elif self.board.board[i][j+1] == player.state:
                if self.board.board[i][j+2] == player.state:
                    self.winner = player
                    
        elif i == 0 and j == 2:
             if self.board.board[i+1][j-1] == player.state:
                if self.board.board[i+2][j-2] == player.state:
                    self.winner = player
             elif self.board.board[i+1][j] == player.state:
                if self.board.board[i+2][j] == player.state:
                    self.winner = player
             elif self.board.board[i][j-1] == player.state:
                if self.board.board[i][j-2] == player.state:
                    self.winner = player
                    
        elif i == 2 and j == 0:
             if self.board.board[i-1][j+1] == player.state:
                if self.board.board[i-2][j+2] == player.state:
                    self.winner = player
             elif self.board.board[i-1][j] == player.state:
                if self.board.board[i-2][j] == player.state:
                    self.winner = player
             elif self.board.board[i][j+1] == player.state:
                if self.board.board[i][j+2] == player.state:
                    self.winner = player
                    
        elif i == 2 and j == 2:
             if self.board.board[i-1][j-1] == player.state:
                if self.board.board[i-2][j-2] == player.state:
                    self.winner = player
             elif self.board.board[i-1][j] == player.state:
                if self.board.board[i-2][j] == player.state:
                    self.winner = player
             elif self.board.board[i][j-1] == player.state:
                if self.board.board[i][j-2] == player.state:
                    self.winner = player
                    
        elif i == 0:
            if self.board.board[i+1][j] == player.state:
                if self.board.board[i+2][j] == player.state:
                    self.winner = player
            elif self.board.board[i][j-1] == player.state:
                if self.board.board[i][j+1] == player.state:
                    self.winner = player
        elif i == 2:
            if self.board.board[i-1][j] == player.state:
                if self.board.board[i-2][j] == player.state:
                    self.winner = player
            elif self.board.board[i][j-1] == player.state:
                if self.board.board[i][j+1] == player.state:
                    self.winner = player
        elif j == 0:
            if self.board.board[i][j+1] == player.state:
                if self.board.board[i][j+2] == player.state:
                    self.winner = player
            elif self.board.board[i-1][j] == player.state:
                if self.board.board[i+1][j] == player.state:
                    self.winner = player
        elif j == 2:
            if self.board.board[i+1][j] == player.state:
                if self.board.board[i-1][j] == player.state:
                    self.winner = player
            elif self.board.board[i][j-1] == player.state:
                if self.board.board[i][j-2] == player.state:
                    self.winner = player
        else:
            if self.board.board[i+1][j+1] == player.state:
                if self.board.board[i-1][j-1] == player.state:
                    self.winner = player
            elif self.board.board[i-1][j+1] == player.state:
                if self.board.board[i+1][j-1] == player.state:
                    self.winner = player
            elif self.board.board[i][j+1] == player.state:
                if self.board.board[i][j-1] == player.state:
                    self.winner = player
            elif self.board.board[i+1][j] == player.state:
                if self.board.board[i-1][j] == player.state:
                    self.winner = player
    
    def fill_square(self, player):
        print("choose square to fill (row,column)")
        row = input("row (0-2):")
        column = input("column (0-2):")
        if self.board.board[i][j] == '-':
            print("setting square {},{} with value {}".format(row, column, player.state))
            self.board.board[i][j] = player.state
            self.winner = self.check_win(player, i, j)
            
    def game_loop(self, choice):
        self.choice = choice
        if self.choice == 0:
            self.player_1.turn = True
        else:
            self.player_2.turn = True
            
        while self.winner == None:
            if self.player_1.turn == True:
                self.fill_square(self.player_1)
            elif self.player_2.turn == True:
                self.fill_square(self.player_2)
                
        print("GAME OVER! {} WINS!".format(self.winner))
                
    def start_game(self):
        print("TIC TAC TOE")
        choice = random.choice([0, 1])
        if choice == 0:
            print("X starts the game!")
            self.game_loop(choice)
        else:
            print("O starts the game!")
            self.game_loop(choice)
            
        