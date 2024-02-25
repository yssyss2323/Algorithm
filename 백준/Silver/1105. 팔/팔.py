l, r = input().split()
if len(l) != len(r):
    print(0)
else:
    for i in range(len(l)):
        if l[i] != r[i]:
            print(l[:i].count('8'))
            break
    else:
        print(l.count('8'))