n = int(input())
for i in range(n // 2, n + 1):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if n == tmp:
        print(i)
        break
else:
    print(0)
