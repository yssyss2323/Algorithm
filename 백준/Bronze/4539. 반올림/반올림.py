def solv(x):
    if len(x) == 1:
        return int(x)
    if int(x[1:]) <= int('4' * (len(x) - 1)):
        return int(x[0] + '0' * (len(x) - 1))
    return int(str(int(x[0]) + 1) + '0' * (len(x) - 1))


for _ in range(int(input())):
    print(solv(input()))