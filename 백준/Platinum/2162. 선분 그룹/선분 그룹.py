def find_func(point1, point2):
    a = point1[1] - point2[1]
    b = point2[0] - point1[0]
    c = - point1[1] * b - point1[0] * a
    return a, b, c

def func_val(a, b, c, point):
    return a * point[0] + b * point[1] + c

def range_check(line1, line2):
    rev_line1 = [[line1[0][1], line1[0][0]], [line1[1][1], line1[1][0]]]
    rev_line2 = [[line2[0][1], line2[0][0]], [line2[1][1], line2[1][0]]]
    line1.sort()
    line2.sort()
    rev_line1.sort()
    rev_line2.sort()
    if (line1[0][0] > line2[1][0] or line1[1][0] < line2[0][0] or
            rev_line1[0][0] > rev_line2[1][0] or rev_line1[1][0] < rev_line2[0][0]):
        return True
    else:
        return False

def relation(line1, line2):
    if range_check(line1, line2):
        return 0
    else:
        a1, b1, c1 = find_func(line1[0], line1[1])
        a2, b2, c2 = find_func(line2[0], line2[1])

        point_start = max(line1[0], line2[0])
        point_end = min(line1[1], line2[1])

        start_val1 = func_val(a1, b1, c1, point_start)
        start_val2 = func_val(a2, b2, c2, point_start)
        end_val1 = func_val(a1, b1, c1, point_end)
        end_val2 = func_val(a2, b2, c2, point_end)

        val1 = start_val1 - start_val2
        val2 = end_val1 - end_val2

        if val1 * val2 > 0:
            return False
        else:
            if (val1 == 0 and val2 != 0) or (val1 != 0 and val2 == 0):
                if b1 == 0:
                    if line2[1][0] == line1[0][0] and line2[1][1] < line1[0][1]:
                        return False
                    if line2[0][0] == line1[0][0] and line2[0][1] > line1[1][1]:
                        return False
                elif b2 == 0:
                    if line1[1][0] == line2[0][0] and line1[1][1] < line2[0][1]:
                        return False
                    if line1[0][0] == line2[0][0] and line1[0][1] > line2[1][1]:
                        return False
            return True


def dfs(table, n):
    stack = []
    visited = [False] * n
    group_cnt = 0
    largest = 0
    for i in range(n):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            group_size = 1
            while stack:
                now = stack.pop()
                for j in table[now]:
                    if not visited[j]:
                        stack.append(j)
                        visited[j] = True
                        group_size += 1
            group_cnt += 1
            largest = max(largest, group_size)
    return group_cnt, largest


if __name__ == "__main__":
    import sys
    input = lambda: sys.stdin.readline().rstrip()
    N = int(input())
    lines = []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        lines.append([[a, b], [c, d]])
    my_table = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i < j and relation(lines[i], lines[j]):
                my_table[i].append(j)
                my_table[j].append(i)
            else:
                pass
    answer = dfs(my_table, N)
    print(*answer, sep='\n')
