mw, mb = map(int, input().split())
tw, tb = map(int, input().split())
pw, pb = map(int, input().split())

x = min(mw, tb, pw)
y = min(mb, tw, pb)
ans = min(x, y) * 2
if x != y:
    ans += 1
print(ans)