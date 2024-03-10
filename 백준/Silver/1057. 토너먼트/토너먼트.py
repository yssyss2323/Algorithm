n,a,b = map(int,input().split())
i = 1
while True:
    if (a-1) // 2**i == (b-1) // 2**i:
        print(i)
        break
    else:
        i += 1