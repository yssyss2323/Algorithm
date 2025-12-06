ans = -1
for _ in range(int(input())):
    tot = sum(list(map(int, input().split())))
    if tot == 512:
        print(512)
        break
    elif tot > 512:
        if ans == -1:
            ans = tot
        elif ans > tot:
            ans = tot
else:
    print(ans)