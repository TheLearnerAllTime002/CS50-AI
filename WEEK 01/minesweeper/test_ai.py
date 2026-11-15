import random
from minesweeper import Minesweeper, MinesweeperAI

wins = 0
games = 50
for _ in range(games):
    game = Minesweeper(height=8, width=8, mines=8)
    ai = MinesweeperAI(height=8, width=8)
    lost = False
    while True:
        move = ai.make_safe_move()
        if move is None:
            move = ai.make_random_move()
        if move is None:
            break
        if game.is_mine(move):
            lost = True
            break
        ai.add_knowledge(move, game.nearby_mines(move))
        if game.won():
            wins += 1
            break
    if not lost:
        wins += 1
print(f"AI won {wins}/{games} games (8x8, 8 mines)")
