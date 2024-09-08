def func(n, curr):
    global ans, arr
    if curr == n:
        ans += 1
    else:
        for i in range(n):
            flag = False
            for x, y in enumerate(arr):
                if i == y or abs(curr - x) == abs(i - y):
                    flag = True
                    break
            if flag:
                continue
            arr.append(i)
            func(n, curr + 1)
            arr.pop()

n = int(input())
arr = []
ans = 0
func(n, 0)
print(ans)