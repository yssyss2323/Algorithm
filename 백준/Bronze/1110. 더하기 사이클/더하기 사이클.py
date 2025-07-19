n = int(input())

ans = 0
nn = n
while True:
    ans += 1
    tmp = (nn % 10) * 10 + (nn // 10 + nn % 10) % 10
    if n == tmp:
        print(ans)
        break
    else:
        nn = tmp