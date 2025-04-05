n, p, q = map(int, input().split())
memo = dict()

def dfs(x):
    if x == 0:
        return 1
    if x in memo:
        return memo[x]
    memo[x] = dfs(x // p) + dfs(x // q)
    return memo[x]

print(dfs(n))