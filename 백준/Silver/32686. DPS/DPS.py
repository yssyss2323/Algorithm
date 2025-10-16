import sys
input = sys.stdin.readline

n, s, e = map(int, input().split())
tot = 0
for _ in range(n):
    r, a, d = map(int, input().split())

    rep1 = e // (r + a)
    rem1 = max(e % (r + a) - r, 0)

    dam = d * rep1
    if rem1 > 0:
        dam += d * rem1 / a

    rep2 = s // (r + a)
    rem2 = max(s % (r + a) - r, 0)

    not_dam = d * rep2
    if rem2 > 0:
        not_dam += d * rem2 / a

    tot += dam - not_dam
print(tot / (e - s))