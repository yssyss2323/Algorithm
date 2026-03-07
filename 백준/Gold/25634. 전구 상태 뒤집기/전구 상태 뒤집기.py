n = int(input())
arr = list(map(int, input().split()))
state = list(map(int, input().split()))
ans = 0
for i in range(n):
    if state[i] == 0:
        arr[i] = -arr[i]
    else:
        ans += arr[i]

prefix_sum = [0]
tmp = 0
for i in range(n):
    tmp += arr[i]
    prefix_sum.append(tmp)

gap = float('inf')
curr_min = float('inf')

for i in range(n):
    curr_min = min(arr[i], curr_min + arr[i])
    gap = min(gap, curr_min)
print(ans - gap)