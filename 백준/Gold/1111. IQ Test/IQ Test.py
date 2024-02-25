n = int(input())
numlist = list(map(int, input().split()))
if n == 1 or (n == 2 and numlist[0] != numlist[1]):
    print('A')
elif n == 2 and numlist[0] == numlist[1]:
    print(numlist[0])
else:
    a = (numlist[2] - numlist[1]) / (numlist[1] - numlist[0]) if numlist[1] != numlist[0] else 0
    if int(a) != a:
        print('B')
        exit()
    a = int(a)
    b = numlist[1] - a * numlist[0]
    for i in range(n - 1):
        if numlist[i + 1] != a * numlist[i] + b:
            print('B')
            break
    else:
        print(a * numlist[-1] + b)