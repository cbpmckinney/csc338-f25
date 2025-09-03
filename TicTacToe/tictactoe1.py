import sys

WIN_LINES = [
    [(0,0),(0,1),(0,2)],  # rows
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)],  # cols
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)],  # diagonals
    [(0,2),(1,1),(2,0)]
]


class GameBoard:

    def __init__(self):

        self.entries = [[0, 0, 0], [0, 0, 0], [0, 0 ,0]]
        self.state = 0
        # State 0: Game playing
        # State 1: Player 1 wins
        # State 2: Player 2 wins
        # State 3: draw

    def print(self):

        for i in range(3):
            for j in range(3):
                print(self.entries[i][j],end='')
            print('')



    def checkwin(self) -> int:
        
        for line in WIN_LINES:
            vals = [self.entries[r][c] for r,c in line]
            if vals == [1, 1, 1]:
                self.state = 1
                return 1
            if vals == [2, 2, 2]:
                self.state = 2
                return 2
        if any(0 in row for row in self.entries):
            self.state = 0
            return 0

        self.state = 3
        return 3

        


gb = GameBoard()

xwin = [[1, 2, 0], [1, 0, 0], [1, 0 ,2]]
owin = [[2, 1, 1], [0, 2, 1], [0, 0 ,2]]
draw = [[1, 2, 2], [2, 1, 1], [1, 1 ,2]]
play = [[1, 2, 1], [0, 2, 0], [2, 1 ,0]]

gb.entries = play
gb.print()
print(gb.checkwin())