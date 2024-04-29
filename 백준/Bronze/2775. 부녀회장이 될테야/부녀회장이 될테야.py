pop = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    pop[0][i] = i
for i in range(1, 15):
    tmp = 0
    for j in range(1, 15):
        tmp += pop[i - 1][j]
        pop[i][j] = tmp

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(pop[k][n])
