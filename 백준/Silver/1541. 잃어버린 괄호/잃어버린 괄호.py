exprs = input().split('-')
answer = sum(list(map(int, exprs[0].split('+'))))
for i in range(1, len(exprs)):
    exprs[i] = sum(list(map(int, exprs[i].split('+'))))
    answer -= exprs[i]
print(answer)
