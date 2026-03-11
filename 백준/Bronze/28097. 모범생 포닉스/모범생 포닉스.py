n = int(input())
times = list(map(int, input().split()))

tot = 8 * (n - 1) + sum(times)
print(tot // 24, tot % 24)