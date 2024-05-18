def bt(given, arr, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        tmp = given[i]
        if arr and arr[-1] > tmp:
            continue
        arr.append(tmp)
        bt(given, arr, n, m)
        arr.pop()


N, M = map(int, input().split())
given_arr = list(map(int, input().split()))
given_arr.sort()
bt(given_arr, [], N, M)
