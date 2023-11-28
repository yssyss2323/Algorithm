import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
arr = []
for _ in range(K):
    callednum = int(input())
    if callednum != 0:
        arr.append(callednum)
    else:
        arr.pop()
print(sum(arr))