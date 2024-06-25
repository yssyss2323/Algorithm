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

def change_map(matrix, point1, point2):  # 2차원 행렬의 인접한 두값 교환한 새로운 2차원행렬 반환 함수
    new_matrix = [line[:] for line in matrix]  # 깊은복사를 위함
    tmp = new_matrix[point2[0]][point2[1]]
    new_matrix[point2[0]][point2[1]] = new_matrix[point1[0]][point1[1]]
    new_matrix[point1[0]][point1[1]] = tmp
    return new_matrix


n = int(input())
candy = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n - 1):
        new_candy = change_map(candy, [i, j], [i, j + 1])
        ans = max(ans, find_longest(new_candy))
for i in range(n - 1):
    for j in range(n):
        new_candy = change_map(candy, [i, j], [i + 1, j])
        ans = max(ans, find_longest(new_candy))
print(ans)
