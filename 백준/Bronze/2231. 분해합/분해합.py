n = int(input())
for i in range(max(n - len(str(n)) * 9, 1), n + 1):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if n == tmp:
        print(i)
        break
else:
    print(0)
