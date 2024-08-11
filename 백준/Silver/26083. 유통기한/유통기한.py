def check(a, b, c):
    if b in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= c <= 31:
            return True
        else:
            return False
    elif b == 2:
        if a % 4:
            if 1 <= c <= 28:
                return True
            else:
                return False
        else:
            if 1 <= c <= 29:
                return True
            else:
                return False
    elif b in [4, 6, 9, 11]:
        if 1 <= c <= 30:
            return True
        else:
            return False
    else:
        return False


def is_safe(a, b, c):
    if a > y:
        return True
    elif a == y:
        if b > m:
            return True
        elif b == m:
            if c >= d:
                return True
    return False


import sys

input = sys.stdin.readline

y, m, d = map(int, input().split())

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if not check(a, b, c) and not check(c, b, a) and not check(c, a, b):
        print("invalid")
    else:
        if check(a, b, c):
            if not is_safe(a, b, c):
                print("unsafe")
                continue
        if check(c, b, a):
            if not is_safe(c, b, a):
                print("unsafe")
                continue
        if check(c, a, b):
            if not is_safe(c, a, b):
                print("unsafe")
                continue
        print("safe")
