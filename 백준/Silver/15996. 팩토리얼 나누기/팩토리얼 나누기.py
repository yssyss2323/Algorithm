n, a = map(int, input().split())

cnt, aa = 0, a
for k in range(31):
    cnt += n // aa
    aa *= a
    if aa > n:
        break
print(cnt)