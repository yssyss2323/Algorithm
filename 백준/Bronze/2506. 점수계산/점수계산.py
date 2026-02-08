n = int(input())
arr = list(map(int, input().split()))

seq = 0
tot = 0
for i in range(n):
    if arr[i] == 0:
        seq = 0
    else:
        seq += 1
        tot += seq
print(tot)