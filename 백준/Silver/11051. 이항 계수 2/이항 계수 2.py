N, K = map(int, input().split())
comb_matrix = [[1] * (x + 1) for x in range(N + 1)]
comb_matrix[0].append(1)
for i in range(N + 1):
    for j in range(i + 1):
        if j == 0 or j == i:
            pass
        else:
            comb_matrix[i][j] = (comb_matrix[i - 1][j - 1] + comb_matrix[i - 1][j]) % 10007

print(comb_matrix[N][K])
