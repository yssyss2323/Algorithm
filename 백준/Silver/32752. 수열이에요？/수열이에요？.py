import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
if sorted(arr) == arr[:l - 1] + sorted(arr[l - 1:r]) + arr[r:n]:
    print(1)
else:
    print(0)
