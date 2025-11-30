import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(m)]
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

for _ in range(k):
    tmp = {}
    for i in range(len(fireball)):
        r, c, m, s, d = fireball[i]
        nr, nc = (r + directions[d][0] * s) % n, (c + directions[d][1] * s) % n
        tmp[(nr, nc)] = tmp.get((nr, nc), [set(), [], [], []])
        tmp[(nr, nc)][0].add(d % 2)
        tmp[(nr, nc)][1].append(m)
        tmp[(nr, nc)][2].append(s)
        tmp[(nr, nc)][3].append(d)
    fireball = []
    for key in tmp.keys():
        curr = tmp[key]
        if len(curr[1]) > 1:
            if sum(curr[1]) // 5 == 0:
                continue
            else:
                if len(curr[0]) == 1:
                    for j in [0, 2, 4, 6]:
                        fireball.append([key[0], key[1], sum(curr[1]) // 5, sum(curr[2]) // len(curr[1]), j])
                else:
                    for j in [1, 3, 5, 7]:
                        fireball.append([key[0], key[1], sum(curr[1]) // 5, sum(curr[2]) // len(curr[1]), j])
        else:
            fireball.append([key[0], key[1], curr[1][0], curr[2][0], curr[3][0]])

ans = 0
for fire in fireball:
    ans += fire[2]
print(ans)