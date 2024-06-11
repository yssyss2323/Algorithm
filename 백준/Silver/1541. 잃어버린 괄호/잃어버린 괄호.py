exprs = input().split('-')
answer = 0
for i in range(len(exprs)):
    exprs[i] = sum(list(map(int, exprs[i].split('+'))))
    if i == 0:
        answer += exprs[i]
    else:
        answer -= exprs[i]
print(answer)
