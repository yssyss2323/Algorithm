a, b = map(int, input().split())

ans = abs((a - 1) // 4 - (b - 1) // 4 ) + abs((a - 1) % 4 - (b - 1) % 4)
print(ans)