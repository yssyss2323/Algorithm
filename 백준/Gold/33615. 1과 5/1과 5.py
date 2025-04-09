import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    num = list(map(int, input()))
    if sum(num) % 3 == 0:
        print(0, 3)
    else:
        if 5 not in num:
            if len(num) % 2 == 0:
                print(0, 11)
            else:
                print(1, 11)
        else:
            if num[-1] == 5:
                print(0, 5)
            else:
                if sum(num) % 3 == 1:
                    print(num.index(1) + 1, 3)
                else:
                    print(num.index(5) + 1, 3)