import sys
input = sys.stdin.readline

p = int(input())
n = int(input())
arr = [0] * 100
for _ in range(n):
    s, d = input().split()
    if d == 'R':
        for i in range(int(s), 100):
            arr[i] = (arr[i] + 1) % 3
    else:
        for i in range(int(s) - 2, -1, -1):
            arr[i] = (arr[i] + 1) % 3
for i in range(3):
    print(f"{p * arr.count(i) / 100:.2f}")
