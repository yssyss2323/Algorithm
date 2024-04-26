def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def disjoint(x, y):
    tmp = gcd(x, y)
    return x // tmp, y // tmp

def lcm(x, y):
    tmp = gcd(x, y)
    return x * y // tmp

def lcm_factor(x, y):
    tmp = lcm(x, y)
    return tmp // x, tmp // y

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for i, connected in enumerate(graph[start]):
        if connected and i not in visited:
            dfs(graph, i, visited)
    return visited

N = int(input())
recipe = [0] * N
relation = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    p, q = disjoint(p, q)
    if recipe[a] and recipe[b]:
        p_tmp, q_tmp = lcm_factor(recipe[a], recipe[b])
        p_factor, q_factor = disjoint(p * p_tmp, q * q_tmp)
        for i in dfs(relation, a):
            recipe[i] *= p_factor
        for i in dfs(relation, b):
            recipe[i] *= q_factor
    elif recipe[a]:
        recipe_factor, pq_factor = lcm_factor(recipe[a], p)
        for i in dfs(relation, a):
            recipe[i] *= recipe_factor
        recipe[b] = q * pq_factor
    elif recipe[b]:
        recipe_factor, pq_factor = lcm_factor(recipe[b], q)
        for i in dfs(relation, b):
            recipe[i] *= recipe_factor
        recipe[a] = p * pq_factor
    else:
        recipe[a] = p
        recipe[b] = q
    relation[a][b], relation[b][a] = True, True
print(*recipe)
