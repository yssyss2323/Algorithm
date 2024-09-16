n = int(input())
hlist = list(map(int, input().split()))
tot = sum(hlist)

if tot % 3:
    print("NO")
else:
    check = 0
    for h in hlist:
        check += h // 2
        if check >= tot // 3:
            print("YES")
            break
    else:
        print("NO")