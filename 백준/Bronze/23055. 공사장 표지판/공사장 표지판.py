n = int(input())
for i in range(n):
    if i in (0, n - 1):
        print('*' * n)
    else:
        line = ""
        for j in range(n):
            if j in (0, n - 1):
                line += "*"
            elif j in (i, n - 1 - i):
                line += "*"
            else:
                line += " "
        print(line)