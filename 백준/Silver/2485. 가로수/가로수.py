def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

n = int(input())
trees = []
for _ in range(n):
    trees.append(int(input()))
numlist = [trees[i + 1] - trees[i] for i in range(n - 1)]

tmp = numlist[0]
for i in range(n - 1):
    tmp = gcd(tmp, numlist[i])

ans = 0
for num in numlist:
    ans += num // tmp - 1
print(ans)