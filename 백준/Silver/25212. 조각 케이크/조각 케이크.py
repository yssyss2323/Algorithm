n = int(input())
cakes = list(map(lambda x: 1 / int(x), input().split()))

ans = 0
def bt(arr, cnt):
    global ans
    if cnt == n:
        if 0.99 <= sum(arr) <= 1.01:
            ans += 1
    else:
        bt(arr, cnt + 1)
        bt(arr + [cakes[cnt]], cnt + 1)

bt([], 0)
print(ans)