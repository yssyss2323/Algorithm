mod = 10 ** 9 + 7

def func(m):
    ans = 2
    for _ in range(m):
        ans = ans * ans
        ans %= mod
    return ans

def pow(m):
    tmp = bin(m)[2:]
    length = len(tmp)
    ans = 1
    for i in range(length):
        if tmp[i] == '1':
            ans *= func(length - i - 1)
            ans %= mod
    return ans


n = int(input())
ans = 0
for _ in range(n):
    c, k = map(int, input().split())
    tmp = c * k * pow(k - 1)
    ans += tmp
    ans %= mod
print(ans)