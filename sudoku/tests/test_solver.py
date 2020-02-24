from sudoku import *

s = Sudoku(9, [(0, 2, 5), (0, 6, 8), (1, 0, 4), (1, 1, 1), (1, 7, 6), (1, 8, 9),
(2, 3, 3), (2, 5, 9), (3, 0, 6), (3, 3, 5), (3, 5, 2), (3, 8, 1), (4, 2, 3), (4, 3, 1), (4, 5, 4),
(4, 6, 2), (5, 2, 2), (5, 6, 4), (6, 2, 7), (6, 3, 8), (6, 5, 6), (6, 6, 9), (7, 4, 1), (8, 1, 2),
(8, 3, 9), (8, 5, 5), (8, 7, 7)])


s.print()
to_do = True
while to_do:
	print("Thinking")
	to_do = s.think()
s.print()

for u in s.unsolved():
	print(f"[{u.row},{u.col}] could be {u.possibilities}")


