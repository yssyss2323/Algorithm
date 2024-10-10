n, m = map(int, input().split())
office = []
cctvs = []
check = []
table = [[False] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    office.append(tmp)
    for j in range(m):
        if tmp[j] in (1,2,3,4,5):
            cctvs.append((i, j))
            check.append(tmp[j])
        if tmp[j] == 6:
            table[i][j] = 'wall'


def counting(table):
    cnt = 0
    for row in table:
        cnt += row.count(False)
    return cnt

def row_p(table, x, y):
    tmp_table = [[i for i in row] for row in table]
    for i in range(y, len(table[0])):
        if office[x][i] == 6:
            break
        else:
            tmp_table[x][i] = True
    return tmp_table


def row_m(table, x, y):
    tmp_table = [[i for i in row] for row in table]
    for i in range(y, -1, -1):
        if office[x][i] == 6:
            break
        else:
            tmp_table[x][i] = True
    return tmp_table


def col_p(table, x, y):
    tmp_table = [[i for i in row] for row in table]
    for i in range(x, len(table)):
        if office[i][y] == 6:
            break
        else:
            tmp_table[i][y] = True
    return tmp_table


def col_m(table, x, y):
    tmp_table = [[i for i in row] for row in table]
    for i in range(x, -1, -1):
        if office[i][y] == 6:
            break
        else:
            tmp_table[i][y] = True
    return tmp_table


ans = float('inf')
def bt(table, x):
    global ans
    if x == len(cctvs):
        cand_ans = counting(table)
        if ans > cand_ans:
            ans = cand_ans
    else:
        curr_tv = cctvs[x]
        if check[x] == 1:
            bt(row_p(table, *curr_tv), x + 1)
            bt(row_m(table, *curr_tv), x + 1)
            bt(col_p(table, *curr_tv), x + 1)
            bt(col_m(table, *curr_tv), x + 1)
        elif check[x] == 2:
            bt(row_m(row_p(table, *curr_tv), *curr_tv), x + 1)
            bt(col_m(col_p(table, *curr_tv), *curr_tv), x + 1)
        elif check[x] == 3:
            bt(col_m(row_p(table, *curr_tv), *curr_tv), x + 1)
            bt(row_p(col_p(table, *curr_tv), *curr_tv), x + 1)
            bt(col_p(row_m(table, *curr_tv), *curr_tv), x + 1)
            bt(row_m(col_m(table, *curr_tv), *curr_tv), x + 1)
        elif check[x] == 4:
            bt(row_m(col_m(row_p(table, *curr_tv), *curr_tv), *curr_tv), x + 1)
            bt(col_m(row_p(col_p(table, *curr_tv), *curr_tv), *curr_tv), x + 1)
            bt(row_p(col_p(row_m(table, *curr_tv), *curr_tv), *curr_tv), x + 1)
            bt(col_p(row_m(col_m(table, *curr_tv), *curr_tv), *curr_tv), x + 1)
        else:
            bt(col_m(row_p(col_p(row_m(table, *curr_tv), *curr_tv), *curr_tv), *curr_tv), x + 1)
            
bt(table, 0)
print(ans)