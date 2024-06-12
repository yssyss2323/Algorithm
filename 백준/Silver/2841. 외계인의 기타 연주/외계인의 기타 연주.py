import sys
input = sys.stdin.readline

N, P = map(int, input().split())
melody = [None] + [[0] for _ in range(6)]
cnt = 0
for _ in range(N):
    line, pret = map(int, input().split())

    while melody[line][-1] > pret:
        melody[line].pop()
        cnt += 1

    if melody[line][-1] < pret:
        melody[line].append(pret)
        cnt += 1

print(cnt)
