def check(sq1, sq2):
    is_not_meet = (sq1[2] < sq2[0] or sq1[3] < sq2[1]) \
              or (sq1[0] > sq2[2] or sq1[1] > sq2[3]) \
              or (sq1[0] > sq2[0] and sq1[1] > sq2[1] and sq1[2] < sq2[2] and sq1[3] < sq2[3]) \
                  or (sq1[0] < sq2[0] and sq1[1] < sq2[1] and sq1[2] > sq2[2] and sq1[3] > sq2[3])
    return not is_not_meet

n = int(input())
coord = [[0,0,0,0]]
relation = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(i):
        if check(coord[j], tmp):
            relation[j].append(i)
            relation[i].append(j)
    coord.append(tmp)

visited = [True] + [False] * n
stack = [0]
while stack:
    curr = stack.pop()
    nxt = relation[curr]
    for nnn in nxt:
        if not visited[nnn]:
            visited[nnn] = True
            stack.append(nnn)

ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        stack.append(i)
        visited[i] = True
        while stack:
            curr = stack.pop()
            nxt = relation[curr]
            for nnn in nxt:
                if not visited[nnn]:
                    visited[nnn] = True
                    stack.append(nnn)
        ans += 1
print(ans)