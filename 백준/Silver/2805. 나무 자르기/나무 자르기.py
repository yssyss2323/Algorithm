N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
sum_trees = [0]
tmp1, tmp2 = 0, 0
for i in range(N - 1):
    tmp1 = (trees[i] - trees[i + 1]) * (i + 1)
    tmp2 += tmp1
    sum_trees.append(tmp2)
for i in range(N):
    check = sum_trees[i]
    if check == M:
        print(trees[i])
        break
    elif check > M:
        n = (check - M) // i
        print(trees[i] + n)
        break
else:
    i = (M - check) // N
    if (M - check) % N:
        i += 1
    print(trees[N - 1] - i)
