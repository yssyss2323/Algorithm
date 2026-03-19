n = int(input())
board = [list(input()) for _ in range(n)]

for i in range(n):
    curr1, curr2 = board[i][0], board[0][i]
    cnt1, cnt2 = 1, 1
    flag = False
    for j in range(1, n):
        if curr1 == board[i][j] and board[i][j] != '.':
            cnt1 += 1
            if cnt1 == 3:
                print(curr1)
                flag = True
                break
        else:
            curr1 = board[i][j]
            cnt1 = 1
        if curr2 == board[j][i] and board[j][i] != '.':
            cnt2 += 1
            if cnt2 == 3:
                print(curr2)
                flag = True
                break
        else:
            curr2 = board[j][i]
            cnt2 = 1
    if flag:
        break
else:
    board2 = [['.'] * n + board[i] + ['.'] * n for i in range(n)]
    for i in range(3, 2 * n - 2):
        curr1, curr2 = board2[0][i], board2[n - 1][i]
        cnt1, cnt2 = 1, 1
        flag = False
        for j in range(1, n):
            if curr1 == board2[j][i + j] and board2[j][i + j] != '.':
                cnt1 += 1
                if cnt1 == 3:
                    print(curr1)
                    flag = True
                    break
            else:
                curr1 = board2[j][i + j]
                cnt1 = 1
            if curr2 == board2[n - 1 - j][i + j] and board2[n - 1 - j][i + j] != '.':
                cnt2 += 1
                if cnt2 == 3:
                    print(curr2)
                    flag = True
                    break
            else:
                curr2 = board2[n - 1 - j][i + j]
                cnt2 = 1
        if flag:
            break
    else:
        print("ongoing")