import sys
input = sys.stdin.readline


tests = [int(input()) for _ in range(int(input()))]
max_n = max(tests)

tmp = [1] * (max_n + 1)
memo = [0] * (max_n + 1)
memo[1] = 1
for i in range(2, max_n + 1):
    for j in range(1, max_n // i + 1):
        tmp[i * j] = tmp[i * j] + i
    memo[i] = memo[i - 1] + tmp[i]

for test in tests:
    print(memo[test])