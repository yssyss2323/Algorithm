n = int(input())

dp = [0, 1]
for _ in range(n):
    dp.append((dp[-1] + dp[-2]) % 15746)
print(dp[-1])