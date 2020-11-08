class Player():
    def __init__(self, state, turn = False):
        '''
            init function for Player class
            
            state: string, should be either X or O
            turn: boolean, initially set to false.
                  if True, then its the user's turn
        '''
        self.state = state
        self.turn = turn
        print("Created player {}".format(self.state))
        
        
    def __repr__(self):
        return self.state
    
    