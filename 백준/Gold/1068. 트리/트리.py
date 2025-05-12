n = int(input())
arr = list(map(int, input().split()))
num = int(input())

relation = [[False] * n for _ in range(n)]
root = []
for i in range(n):
    if arr[i] != -1:
        relation[arr[i]][i] = True
    else:
        root.append(i)

stack = [num]
removed = [False] * n
removed[num] = True
while stack:
    curr = stack.pop()
    for i in range(n):
        if relation[curr][i]:
            stack.append(i)
            removed.append(i)
            relation[curr][i] = False

ans = 0
if not removed[root[0]]:
    while root:
        curr = root.pop()
        flag = True
        for i in range(n):
            if relation[curr][i] and not removed[i]:
                root.append(i)
                flag = False
        if flag:
            ans += 1
print(ans)
