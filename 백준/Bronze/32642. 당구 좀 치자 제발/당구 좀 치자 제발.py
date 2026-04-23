n = int(input())
arr = list(map(int, input().split()))
tot = 0
curr = 0
for i in range(n):
    if arr[i] == 0:
        curr -= 1
    else:
        curr += 1
    tot += curr
print(tot)