import sys
input = sys.stdin.readline


N, P = map(int, input().split())
melody = [None] + [[] for  _ in range(6)]
cnt = 0
for _ in range(N):
    line, pret = map(int, input().split())

    if not melody[line]:
        melody[line].append(pret)
        cnt += 1
    else:
        while melody[line]:
            last_pret = melody[line][-1]
            if last_pret > pret:
                melody[line].pop()
                cnt += 1
            elif last_pret < pret:
                melody[line].append(pret)
                cnt += 1
                break
            else:
                break
        else:
            melody[line].append(pret)
            cnt += 1

print(cnt)
