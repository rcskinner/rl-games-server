import numpy as np

from src.connect4 import connect4

def test_board_init():
    # Check that the board is created and has the appropriate shape
    b = connect4()
    assert b.board.shape == (6,7)

def test_add_peice():
    b = connect4() 
    b.add_peice(0,1)
    assert b.board[0,0] == 1 