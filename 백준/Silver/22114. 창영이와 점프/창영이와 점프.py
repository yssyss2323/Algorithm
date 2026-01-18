n, k = map(int, input().split())
arr = list(map(int, input().split()))#  + [0]

check = []
curr = 1
for i in range(n - 1):
    if arr[i] <= k:
        curr += 1
    else:
        check.append(curr)
        curr = 1
check.append(curr)

if len(check) == 1:
    print(check[0])
elif len(check) == 2:
    print(check[0] + check[1])
else:
    ans = -1
    for i in range(len(check) - 1):
        if check[i] + check[i + 1] > ans:
            ans = check[i] + check[i + 1]
    print(ans)