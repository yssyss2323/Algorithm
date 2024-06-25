import sys
input = lambda:sys.stdin.readline().rstrip()

def find_longest(matrix):
    # 한 라인에서 연속된 색깔 최대개수 구하는 함수
    def find_long(line):
        n = len(line)
        stack = [line[0]]
        tmplength, maxlength = 1, 1
        for i in range(1, n):
            if stack[-1] == line[i]:
                tmplength += 1
                maxlength = max(tmplength, maxlength)
            else:
                tmplength = 1
            stack.append(line[i])
        return maxlength

    # 맵 전체에서 연속된 색깔 최대개수 구하는 함수
    ans = 0
    for row in matrix:
        ans = max(ans, find_long(row))
    for i in range(len(matrix[0])):
        col = [matrix[j][i] for j in range(len(matrix))]
        ans = max(ans, find_long(col))
    return ans


n = int(input())
candy = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n - 1):
        candy1 = candy[i][j]
        candy2 = candy[i][j + 1]
        if candy1 != candy2:
            candy[i][j], candy[i][j + 1] = candy2, candy1
            ans = max(ans, find_longest(candy))
            candy[i][j], candy[i][j + 1] = candy1, candy2
for i in range(n - 1):
    for j in range(n):
        candy1 = candy[i][j]
        candy2 = candy[i + 1][j]
        if candy1 != candy2:
            candy[i][j], candy[i + 1][j] = candy2, candy1
            ans = max(ans, find_longest(candy))
            candy[i][j], candy[i + 1][j] = candy1, candy2
print(ans)
