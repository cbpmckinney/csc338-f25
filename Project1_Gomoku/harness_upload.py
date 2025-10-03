import importlib
import time

import importlib
import time


class GomokuBoard:

    ## this part will be impletmented by you all
    def __init__(self, size=5,win_length=5):
        self.size = size
        self.entries = [[ 0 for _ in range(size)] for _ in range(size)]
        self.last_move = None
        self.win_length = win_length

    def print_bd(self):

        for i in range(self.size):
            for j in range(self.size):
                print(self.entries[i][j],end='')
            print('')

    def copy(self):
        new_board = GomokuBoard()
        new_board.entries = [row[:] for row in self.entries]
        new_board.size = self.size
        new_board.last_move = self.last_move
        new_board.win_length = self.win_length
        return new_board
    
    def check_nextplayer(self, bd = None):
        if bd is None:
            bd = self.entries 
        count_1 = sum(cc == 1 for row in bd for cc in row)
        count_2 = sum(cc == 2 for row in bd for cc in row)
        return 1 if count_1 == count_2 else 2
    
    def in_bounds(self, r,c):
        return 0 <= r < self.size and 0 <= c < self.size
    

    def is_valid_move(self, r, c):
        # return True if (r,c) is a valid empty spot on the board
        return 0 <= r < self.size and 0 <= c < self.size and self.entries[r][c] == 0
    
    def place(self, r, c, player):
        if self.is_valid_move(r, c):
            self.entries[r][c] = player
            self.last_move = (r, c)
            return True
        return False

    def check_winner(self):
        # return 0 if game is still ongoing
        # return 1 if player 1 wins, return 2 if player 2 wins
        # return 3 if draw

        # your code is here
        return 0

class Agent:
    def __init__(self, fn, name=None):
        self.fn = fn
        self.name = name or getattr(fn, "__name__", "Agent")

    def select_move(self, board, time_limit_sec=None):
        # Students get a copy so they can't mutate the official board
        return self.fn(board.copy(), time_limit_sec)
        

def load_agent(module_attr):
    # module_attr must look like "gomoku_team_x:select_move"
    mod, attr = module_attr.split(":")
    module = importlib.import_module(mod)
    fn = getattr(module, attr)
    return Agent(fn, name=f"{mod}.{attr}")

class MatchResult:
    def __init__(self):
        self.moves = []  # (play_idx, player, r, c)
        self.reason = "" # reason why the game is over
        self.winner = 0         
        self.invalid_move_by = None # return the player who made illegal move
        self.timeout_by = None # return the player who exceeded time limit
        self.elapsed_sec = 0.0 # total game time

def play_game(agent_X, agent_O, size, win_length, max_time, show_moves=True):
    board = GomokuBoard(size=size, win_length=win_length)
    result = MatchResult()
    game_start = time.time()
    max_moves = size * size

    for play in range(max_moves):
        player = board.check_nextplayer()                 # 1 for X, 2 for O
        agent  = agent_X if player == 1 else agent_O

       # attain the move within time limit
        start = time.time()
        move = agent.select_move(board, time_limit_sec=max_time)
        dt = time.time() - start
        if max_time is not None and dt > max_time:
            result.timeout_by = player
            result.reason = "Player %d exceeded time (%.3fs > %ss)." % (player, dt, max_time)
            result.winner = 2 if player == 1 else 1
            break
        
        r, c = int(move[0]), int(move[1])
        
        if not board.place( r, c, player):
            result.invalid_move_by = player
            result.reason = "Player %d made illegal move at (%d,%d)." % (player, r, c)
            result.winner = 2 if player == 1 else 1
            break

        result.moves.append((play, player, r, c))
        outcome = board.check_winner()              

        if show_moves:
            print("[Play %03d] %s -> (%d,%d)" % (play, "X" if player==1 else "O", r, c))
            board.print_bd() 
            
        if outcome != 0:
            result.winner = outcome
            if outcome in (1,2):
                result.reason = "Player %d connected %d stones in a row." % (outcome, win_length)
            elif outcome == 3:
                result.reason = "Draw"
            break

    result.elapsed_sec = time.time() - game_start
    return result
