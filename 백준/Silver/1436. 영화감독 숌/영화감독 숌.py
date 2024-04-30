target = int(input())
if target > 3700:
    t = target // 3700
    idx = t * 3700
    for i in range(t * 10 ** 6, 2666800):
        if '666' in str(i):
            idx += 1
        if idx == target:
            print(i)
            break
else:
    idx = 0
    for i in range(666, 10 ** 6):
        if '666' in str(i):
            idx += 1
        if idx == target:
            print(i)
            break
