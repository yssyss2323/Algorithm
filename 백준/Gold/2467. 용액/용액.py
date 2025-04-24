n = int(input())
arr = list(map(int, input().split()))
r, l = 0, n - 1

val = float('inf')
a, b = r, l
while r < l:
    tmp = arr[r] + arr[l]

    if val > abs(tmp):
        val = abs(tmp)
        a, b = arr[r], arr[l]

    if tmp > 0:
        l -= 1
    elif tmp < 0:
        r += 1
    else:
        print(arr[r], arr[l])
        break
else:
    print(a, b)