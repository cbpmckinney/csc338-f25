import math 
import time
import random

class GomokuBoard:
    def __init__(self, size=5,win_length=5):
        # you can add other objects you need
        self.size = size # size could be vary from 5 to 8
        self.win_length = win_length # win if continuous count is >= win_length
        self.entries = [[ 0 for _ in range(size)] for _ in range(size)]
    
    def is_valid_move(self):
        # return True/False based on whetehr the move is valid 
        # check i) is bounded in the board? ii) is on the empty spots? 
        # your code is here!
        return 

    def check_winner(self):
        # player will win if they have "win_length" or more stones in a row. 
        # return 0:ongoing / 1 or 2: player win / 3: draw
        # your code is here!
        return 
        
    # feel free to add any functions you need


class GomokuGame:

    def __init__(self,time_limit):

        self.gameboard = GomokuBoard()
        
        # elapsed time from when the agent is called until it returns a move
        # if the agent exceeds the time limit, the game immediately ends
        self.time_limit = time_limit

        # define any objects you need
    
    # add any functions you need

# define any class you need

def select_move(bd, time_limit = None):
    # compute (r,c) within time limit
    return (r,c) 