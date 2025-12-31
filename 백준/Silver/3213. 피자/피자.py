import sys
input = lambda:sys.stdin.readline().rstrip()

check = {"1/2":0, "1/4":0, "3/4":0}
ans = 0
for _ in range(int(input())):
    check[input()] += 1

ans += check["3/4"]
check["1/4"] -= min(check["1/4"], check["3/4"])
check["3/4"] -= min(check["1/4"], check["3/4"])

ans += check["1/2"] // 2
if check["1/2"] % 2:
    ans += 1
    if check["1/4"] <= 2:
        print(ans)
    else:
        ans += (check["1/4"] - 2) // 4
        if (check["1/4"] - 2) % 4:
            ans += 1
        print(ans)
else:
    ans += check["1/4"] // 4
    if check["1/4"] % 4:
        ans += 1
    print(ans)