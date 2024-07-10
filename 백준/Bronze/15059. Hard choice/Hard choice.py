ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

ans = 0
if cr > ca:
    ans += cr - ca
if br > ba:
    ans += br - ba
if pr > pa:
    ans += pr - pa
print(ans)