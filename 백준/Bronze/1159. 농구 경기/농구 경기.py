check = dict()
n = int(input())
for _ in range(n):
    tmp = input()
    key = tmp[0]
    val = tmp[1:]
    check[key] = check.get(key, 0) + 1

ans = []
for key in check.keys():
    if check[key] >= 5:
        ans.append(key)
ans.sort()

if ans:
    print(*ans, sep='')
else:
    print('PREDAJA')