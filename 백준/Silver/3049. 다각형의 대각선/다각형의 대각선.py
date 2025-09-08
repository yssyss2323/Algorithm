n = int(input())
ans = 1
for i in range(4):
    ans *= (n - i)
for i in range(1, 5):
    ans //= i
print(ans)