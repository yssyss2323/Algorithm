from math import pi

n = int(input())
pibo = [[0] * (int(i / pi) + 1) for i in range(n + 1)]
pibo[0][-1] = 1
for i in range(n + 1):
    pibo[i][-1] = 1
    for j in reversed(range(len(pibo[i]) - 1)):
        pibo[i][j] = (pibo[i - 1][j] + pibo[i][j + 1]) % 10**18
print(pibo[n][0])