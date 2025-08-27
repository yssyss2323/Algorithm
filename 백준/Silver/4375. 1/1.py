while True:
    try:
        n = int(input())
        x = 1
        ans = 1
        while True:
            if x % n == 0:
                print(ans)
                break
            else:
                x = x * 10 + 1
                ans += 1
    except:
        break
