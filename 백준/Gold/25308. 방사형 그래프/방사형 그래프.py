def is_convex(point1, point2, point3):
    if point2 > point1 * point3 * 2 ** 0.5 / (point1 + point3):
        return True
    else:
        return False

def check(eight_points):
    for i in range(8):
        if not is_convex(eight_points[i - 2], eight_points[i - 1], eight_points[i]):
            return 0
    else:
        return 1

def backtracking(return_arr, visited, stats):
    if len(return_arr) == 7:
        tmp_arr = [7] + return_arr
        final_arr = [stats[i] for i in tmp_arr]
        return check(final_arr) * 8

    answer = 0
    for i in range(7):
        if not visited[i]:
            return_arr.append(i)
            visited[i] = True
            answer += backtracking(return_arr, visited, stats)
            return_arr.pop()
            visited[i] = False

    return answer


if __name__ == "__main__":
    stats = list(map(int, input().split()))
    answer = 0
    print(backtracking([], [False] * 7, stats))
