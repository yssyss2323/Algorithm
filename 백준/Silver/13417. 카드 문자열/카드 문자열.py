t = int(input())
for _ in range(t):
    n = int(input())
    cards = input().split()

    ans = cards[0]
    for i in range(1, n):
        curr = cards[i]
        if curr <= ans[0]:
            ans = curr + ans
        else:
            ans += curr
    print(ans)