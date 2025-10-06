n, k = map(int, input().split())

check = 0
while True:
    curr_check = 9 * 10 ** check * (check + 1)
    if k <= curr_check:
        stand = 10 ** check - 1 + k // (check + 1)
        if stand > n:
            print(-1)
        else:
            if k % (check + 1):
                stand += 1
                if stand > n:
                    print(-1)
                else:
                    print(str(stand)[k % (check + 1) - 1])
            else:
                print(stand % 10)
        break
    else:
        k -= curr_check
        check += 1