def calc(a, b):
    return (100 * b) // a

x, y = map(int, input().split())
z = calc(x, y)
if z >= 99:
    print(-1)
else:
    start, end = 0, x
    while start <= end:
        mid = (start + end) // 2
        if calc(x + mid, y + mid) > z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    print(answer)
