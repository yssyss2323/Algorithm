n = int(input())
nn = int(n ** 0.5)
if nn ** 2 >= n:
    print(nn)
else:
    print(nn + 1)