n, m = map(int, input().split())
check = list(set(map(int, input().split())))
check.sort()
n = len(check)
def bt(arr, length):
    if len(arr) == length:
        print(*arr)
        return

    for i in range(n):
        curr = check[i]
        arr.append(curr)
        bt(arr, length)
        arr.pop()

bt([], m)