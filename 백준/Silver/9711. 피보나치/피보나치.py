import sys
input = sys.stdin.readline


inputs = []
prange = 0

t = int(input())
for i in range(t):
    p, q = map(int, input().split())
    if p > prange:
        prange = p
    inputs.append((p, q))

fibo = [0] * (prange + 1)
fibo[1] = 1
for i in range(2, prange + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

for i in range(1, t + 1):
    p, q = inputs[i - 1]
    print(f"Case #{i}:", fibo[p] % q)