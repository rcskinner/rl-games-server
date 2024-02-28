import numpy as np

class connect4:
    """Create a connect4 board class that operates the game,
    stores game state, and determines win condition
    
    Attributes: 
        - board: Game board 
        - __highest_position: Convenience vector representing the next available 
            position for each column. Initialized with a vector of zeros
    
    Methods: 
        - add_piece: 

    """
    def __init__(self):
        self.board = np.zeros((6,7)).astype(int)
        self.__next_position = np.zeros((1,7)).astype(int)
    
    def add_peice(self,column,player):
        # Get the next position for that column, update board, and update next pos
        next = self.__next_position[0][column]
        self.board[next,column] = player
        self.__next_position[0, column] += 1 

    def get_val(self,row, col):
        return self.board[row,col]

    def check_win(self, row: int, col:int):
        """Check the win conditions after a new peice has been placed.
        Looking for 4 matching peices in a row:
            - Up
            - Down
            - Left
            - Right
            - Diagonally
        """
        # Get the value of the updated position
        val = self.get_val(row, col)

        #Check down
        if row + 4 <= 6:
            checked_array = self.board[row:row+4,col]
            if np.unique(checked_array).shape[0] == 1:
                return "Winner - Down"
        
        # Check down
        if row - 4 >= 0: 
            checked_array = self.board[row-3:row+1,col]
            if np.unique(checked_array).shape[0] == 1:
                return "Winner - Up"