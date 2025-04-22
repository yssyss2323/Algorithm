a, b, c = map(int, input().split())
k, l = map(int, input().split())
bb = b % 6
term = 0
if bb == 1:
    t = 1
elif bb == 2:
    if c % 2 == 1:
        t = 2
    else:
        t = 4
elif bb == 3:
    t = 3
elif bb == 4:
    t = 4
elif bb == 5:
    if c % 2 == 1:
        t = 5
    else:
        t = 1
else:
    t = 0
case1 = (k + a ** t) % 7 == l
bbb = b % 7
cc = c % 6
case2 = (bbb ** cc * a ** 5 + k) % 7 == l

if case1 and case2:
    print(3)
else:
    if case1:
        print(1)
    elif case2:
        print(2)
    else:
        print(0)