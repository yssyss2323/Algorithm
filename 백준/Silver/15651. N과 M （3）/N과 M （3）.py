n, m = map(int, input().split())

def bt(arr, n, m):
    if len(arr) == m:
        print(*arr)
    else:
        for i in range(1, n + 1):
            arr.append(i)
            bt(arr, n, m)
            arr.pop()

bt([], n, m)