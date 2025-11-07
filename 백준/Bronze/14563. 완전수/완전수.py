def check(num):
    tot = 1
    half = int(num ** 0.5)
    for i in range(2, half + 1):
        if num % i == 0:
            tot += i + num // i
    if half ** 2 == num:
        tot -= half

    if tot > num:
        print("Abundant")
    elif tot < num:
        print("Deficient")
    else:
        print("Perfect")


import sys
input = sys.stdin.readline

t = int(input())
numlist = list(map(int, input().split()))

for num in numlist:
    check(num)