x, y, w, s = map(int, input().split())

if 2 * w <= s:
    print((x + y) * w)
else:
    ll, ss = max(x, y), min(x, y)
    if w <= s:
        print(ss * s + (ll - ss) * w)
    else:
        if (ll - ss) % 2:
            print((ll - 1) * s + w)
        else:
            print(ll * s)
