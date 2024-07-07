maxnum = 0
ans = (1,1)
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] > maxnum:
            maxnum = tmp[j]
            ans = (i+1,j+1)
print(maxnum)
print(*ans)