n, m = map(int, input().split())

if n >= m:
    print(0)
else:
    curr = 1
    for i in range(2, n + 1):
        curr = (curr * i) % m
        if curr == 0:
            print(0)
            break
    else:
        print(curr)