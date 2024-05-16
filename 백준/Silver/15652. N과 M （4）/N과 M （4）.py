def bt(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if arr and arr[-1] > i:
            continue
        arr.append(i)
        bt(arr,n,m)
        arr.pop()

N, M = map(int,input().split())
bt([],N,M)