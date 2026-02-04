import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, s = input().split()
    o = 0 if '8' in s or '9' in s else int(s, 8)
    print(k, o, int(s), int(s, 16))