import random
from .Board import Board
from .Player import Player
import time

class Play():
    
    def __init__(self,  choice = 0, winner=None):
        '''
            init function for class
            
            winner: object, to be set with player object who won the game
            choice: int, used to select who starts the game
            player_1: object, to be set as a player object
            player_2: object, to be set as a player object
            board: object, to be set a board object
        '''
        self.winner = winner
        self.choice = choice
        self.player_1 = None
        self.player_2 = None
        self.board = None
#         Player.__init__(self, '.')
        
    def check_win(self, player, i, j):
        '''
            Function to check if player has won the game or not
            
            Check every possible combination in a 3x3 board
            player: player object
            i: int, row value in board
            j: int, column value in board
        '''
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
        '''
            Function to place X/O on the board based on player's input
            
            player: player object
        '''
        print("choose square to fill (row,column)")
        input_flag = False
        while input_flag == False:
            try:    
                row = int(input("row (0-2):"))
                column = int(input("column (0-2):"))
                if row <=2 and row >= 0 and column <=2 and column >= 0:
                    input_flag = True
                else:
                    print("Enter value between 0-2")
            except:
                print("Please Enter a number")
        if self.board.game_board[row][column] == '-':
            print("setting square {},{} with value {}".format(row, column, player.state))
            self.board.game_board[row][column] = player.state
            self.check_win(player, row, column)
        else:
            flag = False
            while flag == False:
                print("Please choose an empty square!")
                print("choose square to fill (row,column)")
                input_flag = False
                while input_flag == False:
                    try:    
                        row = int(input("row (0-2):"))
                        if row <=2 and row >= 0:
                            column = int(input("column (0-2):"))
                            if column <=2 and column >= 0:
                                input_flag = True
                            else:
                                print("Enter value between 0-2")
                        else:
                            print("Enter value between 0-2")
                    except:
                        print("Please Enter a number")
                        
                if self.board.game_board[row][column] == '-':
                    flag = True
            print("setting square {},{} with value {}".format(row, column, player.state))
            self.board.game_board[row][column] = player.state
            self.check_win(player, row, column)
            
    def game_loop(self, choice):
        '''
            Function to start game loop.
            Terminates when one of the players win
            
            choice: int, used to select who starts the game
        '''
        
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
        '''
            Function to start the game of Tic-Tac-Toe
        '''
        self.winner = None
        print("TIC TAC TOE")
        time.sleep(1)
        self.board = Board()
        self.board.initialize_board()
        time.sleep(1)
        self.player_1 = Player('X')
        time.sleep(1)
        self.player_2 = Player('O')
        time.sleep(1)
        choice = random.choice([0, 1])
        if choice == 0:
            print("X starts the game!")
            self.game_loop(choice)
        else:
            print("O starts the game!")
            self.game_loop(choice)
            
        