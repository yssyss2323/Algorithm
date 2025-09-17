n = int(input()) - 1
if n >= 1023:
    print(-1)
else:
    nums = list(map(str, reversed(range(10))))
    anslist = []
    for i in range(1, 2 ** 10):
        check = bin(i)[2:]
        check = (10 - len(check)) * '0' + check
        num = ""
        for j in range(10):
            if check[j] == '1':
                num += nums[j]
        anslist.append(int(num))
    anslist.sort()
    print(anslist[n])