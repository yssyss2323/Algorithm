import sys
input = sys.stdin.readline

memo = [0] * 8000

def recur(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)

    idx = (a-1)*400 + (b-1) * 20 + (c-1)
    if not memo[idx]:
        if a < b < c:
            memo[idx] = recur(a, b, c - 1) + recur(a, b - 1, c - 1) - recur(a, b - 1, c)
        else:
            memo[idx] = recur(a - 1, b, c) + recur(a - 1, b - 1, c) + recur(a - 1, b, c - 1) - recur(a - 1, b - 1, c - 1)

    return memo[idx]


while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break

    print(f"w({a}, {b}, {c}) = {recur(a,b,c)}")