def check_col(col_n, n, l):
    arr = [board[x][col_n] for x in range(n)]
    curr = [arr[0], 1]
    tmp_check = [False] * n
    for i in range(1, n):
        if arr[i] == curr[0]:
            curr[1] += 1
        else:
            if abs(arr[i] - curr[0]) > 1:
                return None
            elif arr[i] > curr[0]:
                if curr[1] < l:
                    return None
                else:
                    for t in range(i - l, i):
                        if tmp_check[t]:
                            return None
                    else:
                        for t in range(i - l, i):
                            tmp_check[t] = True
                        curr = [arr[i], 1]
            else:
                for j in range(1, l):
                    if i + j >= n or arr[i + j] != arr[i]:
                        return None
                else:
                    for t in range(i, i + l):
                        if tmp_check[t]:
                            return None
                    else:
                        for t in range(i, i + l):
                            tmp_check[t] = True
                        curr = [arr[i], 1]
    else:
        return True


def check_row(row_n, n, l):
    arr = board[row_n]
    curr = [arr[0], 1]
    tmp_check = [False] * n
    for i in range(1, n):
        if arr[i] == curr[0]:
            curr[1] += 1
        else:
            if abs(arr[i] - curr[0]) > 1:
                return None
            elif arr[i] > curr[0]:
                if curr[1] < l:
                    return None
                else:
                    for t in range(i - l, i):
                        if tmp_check[t]:
                            return None
                    else:
                        for t in range(i - l, i):
                            tmp_check[t] = True
                        curr = [arr[i], 1]
            else:
                for j in range(1, l):
                    if i + j >= n or arr[i + j] != arr[i]:
                        return None
                else:
                    for t in range(i, i + l):
                        if tmp_check[t]:
                            return None
                    else:
                        for t in range(i, i + l):
                            tmp_check[t] = True
                        curr = [arr[i], 1]
    else:
        return True


n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

ans = 0
for i in range(n):
    if check_row(i, n, l):
        ans += 1
for i in range(n):
    if check_col(i, n, l):
        ans += 1
print(ans)