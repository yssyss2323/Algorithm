N = int(input())
X = list(map(int, input().split()))
check = sorted(list(set(X)))
check_dic = dict()
for idx, val in enumerate(check):
    check_dic[val] = idx
ans = []
for x in X:
    ans.append(check_dic[x])
print(*ans)
