h, m, s = map(int, input().split())
t = int(input())

mm, tt = divmod(t, 60)
hh, mm = divmod(mm, 60)

tmp, s = divmod(s + tt, 60)
tmp, m = divmod(m + mm + tmp, 60)
h = (h + hh + tmp) % 24

print(h, m, s)