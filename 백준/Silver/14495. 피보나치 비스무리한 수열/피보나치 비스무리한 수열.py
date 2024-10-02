n = int(input())

table = [1,1,1]

if n < 4:
    print(table[n - 1])
else:
    for i in range(3, n):
        table.append(table[i - 1] + table[i - 3])
    print(table[-1])