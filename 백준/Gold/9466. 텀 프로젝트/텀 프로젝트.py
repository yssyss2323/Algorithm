import sys
input = sys.stdin.readline

def f(ch):
    return int(ch) - 1

t = int(input())
for _ in range(t):
    n = int(input())
    students = list(map(f, input().split()))
    visited = [-1] * n
    visited2 = [False] * n
    ans = 0
    tmp = 0
    for student in range(n):
        if visited[student] == -1:
            visited[student] = 0
            like = students[student]
            stack = [(like,0)]
            prev = student
            stack2 = [student]
            while stack:
                now, cnt = stack.pop()
                if visited[now] == -1:
                    stack2.append(now)
                    visited[now] = cnt + 1
                    next_student = students[now]
                    stack.append((next_student, cnt + 1))
                    prev = now
                else:
                    if not visited2[now]:
                        ans += visited[now]
                        tmp += cnt +1 - visited[prev]
                    else:
                        ans += cnt + 1
            for i in stack2:
                visited2[i] = True
    print(ans)
