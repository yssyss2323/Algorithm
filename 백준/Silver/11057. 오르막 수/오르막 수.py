n = int(input())
mod = 10007

dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(n - 1):
    tmp = [0] * 10
    for i in range(10):
        tmp[i] = sum(dp[:i + 1]) % mod
    dp = tmp
print(sum(dp) % mod)
