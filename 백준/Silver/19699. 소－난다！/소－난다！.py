n, m = map(int, input().split())
hlist = list(map(int, input().split()))

max_prime = sum(sorted(hlist)[-m:])
check = [False] * 2 + [True] * (max_prime - 1)
for i in range(2, max_prime + 1):
    if check[i]:
        for j in range(i * 2, max_prime + 1, i):
            check[j] = False

ans = set()

def bt(arr, idx):
    if len(arr) == m:
        if check[sum(arr)]:
            ans.add(sum(arr))
        return

    for i in range(n):
        if i <= idx:
            continue
        else:
            arr.append(hlist[i])
            bt(arr, i)
            arr.pop()


bt([], -1)
ans = list(ans)
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)
