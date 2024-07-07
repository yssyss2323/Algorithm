def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


n = int(input())
numlist = list(map(int, input().split()))
numlist.sort()

tmplist = []
for i in range(1, n):
    tmplist.append(numlist[i] - numlist[i - 1])

tmp = tmplist[0]
for i in range(1, n - 1):
    tmp = gcd(tmp, tmplist[i])
print(tmp)
