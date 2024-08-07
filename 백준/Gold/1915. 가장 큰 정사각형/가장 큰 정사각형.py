import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

check = [0] * m
ans_length = 0
for i in range(n):
    curr_row = list(map(int, input()))
    for j in range(m):
        if curr_row[j]:
            check[j] += 1
        else:
            check[j] = 0

    stack = []
    for i in range(m):
        while stack and check[stack[-1]] > check[i]:
            h = check[stack.pop()]
            w = 1 if not stack else i - stack[-1] - 1
            if min(h, w) > ans_length:
                ans_length = min(h, w)
        stack.append(i)

    while stack:
        h = check[stack.pop()]
        w = m if not stack else m - stack[-1] - 1
        if min(h, w) > ans_length:
            ans_length = min(h, w)
print(ans_length ** 2)