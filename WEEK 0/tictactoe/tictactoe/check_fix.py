import tictactoe as ttt

# result edge cases
b = ttt.initial_state()
b[0][0] = ttt.X
for action in [(0, 0), (-1, 0), (0, -1), (3, 0), (0, 3), ("a", "b")]:
    try:
        ttt.result(b, action)
        print(f"FAIL: no exception for {action!r}")
    except Exception:
        pass
# does not modify original
new = ttt.result(b, (1, 1))
assert b[1][1] == ttt.EMPTY
print("result edge cases OK")

# quick minimax sanity + speed
import time
start = time.time()
move = ttt.minimax(ttt.initial_state())
print(f"empty board move: {move} in {time.time()-start:.2f}s")
assert ttt.minimax([["X","X","X"],["O","O",ttt.EMPTY],[ttt.EMPTY,ttt.EMPTY,ttt.EMPTY]]) is None
b2 = [[ttt.EMPTY, ttt.EMPTY, ttt.EMPTY],
      [ttt.EMPTY, "O", "O"],
      [ttt.EMPTY, ttt.EMPTY, "X"]]  # O threatens (1,0)
assert ttt.minimax(b2) == (1, 0), "must block (1,0)"
b3 = [["O", "X", "X"],
      [ttt.EMPTY, "O", ttt.EMPTY],
      [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]]  # X to move
assert ttt.minimax(b3) == (1, 0) or ttt.minimax(b3) == (1, 2) or ttt.minimax(b3) == (2, 0)
print("All checks passed!")
