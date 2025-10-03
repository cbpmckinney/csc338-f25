import time
import importlib

from harness import load_agent, play_game



if __name__ == "__main__":
    
    agentA = load_agent("gomoku_team_1:select_move")
    agentB = load_agent("gomoku_team_2:select_move")

    print("Loaded agents:", agentA.name, "vs", agentB.name)

    
    result = play_game(agentA, agentB, size=5, win_length=5, max_time=3.2, show_moves=True)

    print("\n=== Game Result ===")
    print("Winner:", result.winner)
    print("Reason:", result.reason)
    print("Moves played:", len(result.moves))
    print("Elapsed time: %.3f sec" % result.elapsed_sec)