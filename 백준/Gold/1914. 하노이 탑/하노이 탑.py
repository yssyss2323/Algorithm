def solv(x):
    if x == 1:
        return [[1, 3]]

    arr1, arr2 = [], []
    for move in solv(x - 1):
        tmp1 = [move[0], move[1]]
        if move[0] == 2:
            tmp1[0] = 3
        elif move[0] == 3:
            tmp1[0] = 2
        if move[1] == 2:
            tmp1[1] = 3
        elif move[1] == 3:
            tmp1[1] = 2
        arr1.append(tmp1)

        tmp2 = [move[0], move[1]]
        if move[0] == 2:
            tmp2[0] = 1
        elif move[0] == 1:
            tmp2[0] = 2
        if move[1] == 2:
            tmp2[1] = 1
        elif move[1] == 1:
            tmp2[1] = 2
        arr2.append(tmp2)
    arr1.append([1, 3])
    return arr1 + arr2

n = int(input())
print(2 ** n - 1)
if n <= 20:
    for x in solv(n):
        print(*x)
