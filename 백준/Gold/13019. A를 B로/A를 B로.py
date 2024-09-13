a = list(input())
b = list(input())

if sorted(a) != sorted(b):
    print(-1)
else:
    ans = 0
    stand = 0
    a.reverse()
    b.reverse()
    for ch in b:
        for i in range(stand, len(a)):
            if ch == a[i]:
                idx = i
                ans += idx - stand
                stand = idx + 1
                break
        else:
            ans += len(a) - stand
            break
    print(ans)