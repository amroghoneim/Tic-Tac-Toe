class Player():
    def __init__(self, state, turn = False):
        self.state = state
        self.turn = turn
        
        
    def __repr__(self):
        return self.state
    
    