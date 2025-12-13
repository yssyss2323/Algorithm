n, k = map(int, input().split())
arr = list(map(int, input().split()))

check = dict()
for i in range(n):
    check[arr[i]] = check.get(arr[i], 0) + 1

for i in range(1, n + 1):
    tmp = i
    while tmp > 0:
        if tmp in check.keys() and check[tmp] > 0:
            check[tmp] -= 1
            break
        else:
            tmp -= k
    else:
        print(0)
        break
else:
    print(1)