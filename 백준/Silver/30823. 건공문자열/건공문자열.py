n, k = map(int, input().split())
string = input()
rem = string[:k - 1]
if (n - k) % 2 == 0:
    rem = rem[::-1]
ans = string[k - 1:] + rem
print(*ans, sep='')