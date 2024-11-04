import sys
input = sys.stdin.readline

n = int(input())
arr = [float(input()) for _ in range(n)]
for i in range(1, n):
    if 1 < arr[i - 1]:
        arr[i] *= arr[i - 1]
print(f"{max(arr):.3f}")