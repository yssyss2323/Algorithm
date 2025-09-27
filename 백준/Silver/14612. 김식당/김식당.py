import sys
input = sys.stdin.readline


n, m = map(int, input().split())
table = []
for _ in range(n):
    order = list(input().split())
    if order[0] == "order":
        n, m = map(int, order[1:])
        table.append((n, m))
    elif order[0] == "sort":
        table.sort(key=lambda x:[x[1], x[0]])
    else:
        table_num = int(order[1])
        for i in range(len(table)):
            if table[i][0] == table_num:
                table = table[:i] + table[i + 1:]
                break

    if table:
        for x in table:
            print(x[0], end=' ')
        print()
    else:
        print("sleep")
