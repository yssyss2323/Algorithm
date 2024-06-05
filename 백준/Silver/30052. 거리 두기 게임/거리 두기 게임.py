N, M = map(int, input().split())
D = int(input())

cnt = 0
for i in range(N // 2):
    for j in range(M // 2):
        if (M - 1 + N - 1) - (i + j) < D:
            cnt += 4
if N % 2 == 1:
    for i in range(M // 2):
        if (M - 1 + N - 1) - (N // 2 + i) < D:
            cnt += 2
if M % 2 == 1:
    for i in range(N // 2):
        if (M - 1 + N - 1) - (M // 2 + i) < D:
            cnt += 2
if (N % 2 == 1) and (M % 2 == 1):
    if (M - 1 + N - 1) - (N // 2 + M // 2) < D:
        cnt += 1

print(cnt)
