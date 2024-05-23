def bt(given, arr, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        tmp = given[i]
        if arr and tmp < arr[-1]:
            continue
        arr.append(tmp)
        bt(given, arr, n, m)
        arr.pop()


_, M = map(int, input().split())
given_arr = list(set(map(int, input().split())))
N = len(given_arr)
given_arr.sort()

bt(given_arr, [], N, M)
