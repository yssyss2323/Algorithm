king, rock, n = input().split()
chessmap = [[False] * 10] + [[False] + [True] * 8 + [False] for _ in range(8)] + [[False] * 10]
changelist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
king_pos = [int(changelist.index(king[0])) + 1, int(king[1])]
rock_pos = [int(changelist.index(rock[0])) + 1, int(rock[1])]

orderlist = []
changedic = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
for _ in range(int(n)):
    tmp = input()
    orderlist.append(changedic[tmp])

for order in orderlist:
    next_king_pos = [king_pos[0] + order[0], king_pos[1] + order[1]]
    if next_king_pos == rock_pos:
        next_rock_pos = [rock_pos[0] + order[0], rock_pos[1] + order[1]]
    else:
        next_rock_pos = rock_pos
    if chessmap[next_king_pos[0]][next_king_pos[1]] and chessmap[next_rock_pos[0]][next_rock_pos[1]]:
        king_pos = next_king_pos
        rock_pos = next_rock_pos

final_king_pos = changelist[king_pos[0] - 1] + str(king_pos[1])
final_rock_pos = changelist[rock_pos[0] - 1] + str(rock_pos[1])
print(final_king_pos)
print(final_rock_pos)
