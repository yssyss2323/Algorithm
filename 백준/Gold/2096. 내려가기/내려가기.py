import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
numlist = list(map(int, input().split()))
dp_min = numlist
dp_max = numlist
for i in range(1, n):
    numlist = list(map(int, input().split()))
    dp_min = [min(dp_min[0], dp_min[1]) + numlist[0],
                   min(dp_min[0], dp_min[1], dp_min[2]) + numlist[1],
                   min(dp_min[1], dp_min[2]) + numlist[2]]
    dp_max = [max(dp_max[0], dp_max[1]) + numlist[0],
                   max(dp_max[0], dp_max[1], dp_max[2]) + numlist[1],
                   max(dp_max[1], dp_max[2]) + numlist[2]]
print(max(dp_max), min(dp_min))
