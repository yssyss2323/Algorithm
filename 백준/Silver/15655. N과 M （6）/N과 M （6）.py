n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

def bt(arr, length):
    if len(arr) == length:
        print(*arr)
        return

    for i in range(n):
        curr = num[i]
        if arr and curr <= arr[-1]:
            continue
        arr.append(curr)
        bt(arr, length)
        arr.pop()

bt([], m)