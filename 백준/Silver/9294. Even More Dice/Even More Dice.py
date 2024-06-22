def backtracking(n, m, s, arr):
    if len(arr) == n:
        if sum(arr) == s:
            print('(', end='')
            print(*arr, sep=',', end='')
            print(')')
        #return
    else:
        for i in range(1, m + 1):
            if not arr or arr[-1] <= i:
                arr.append(i)
                backtracking(n, m, s, arr)
                arr.pop()


c = int(input())
for i in range(c):
    print(f"Case {i + 1}:")
    n, m, s = map(int, input().split())
    backtracking(n, m, s, [])
