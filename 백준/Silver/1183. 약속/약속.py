arr = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr.append(a - b)

arr.sort()
def func(arr, n):
    return sum(list(map(lambda x:abs(x + n), arr)))

check = func(arr, -arr[0])
start, end = 0, 0
for i in range(1, n):
    x = arr[i]
    val = func(arr, -x)
    if val < check:
        check = val
        start, end = i, i
    elif val == check:
        end = i
print(arr[end] - arr[start] + 1)