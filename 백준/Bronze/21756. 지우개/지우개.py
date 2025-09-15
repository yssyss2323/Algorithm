n = int(input())

ans = 1
while True:
    if ans * 2 <= n:
        ans *= 2
    else:
        print(ans)
        break