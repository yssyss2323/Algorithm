n, k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = 0
prefix_dic = {0 : 1}
prefix_set = {0}
prefix_arr = [0]
for a in arr:
    tmp += a
    prefix_dic[tmp] = prefix_dic.get(tmp, 0) + 1
    prefix_arr.append(tmp)
    prefix_set.add(tmp)

ans = 0
for elem in prefix_arr:
    if prefix_dic[elem] > 1:
        prefix_dic[elem] -= 1
    else:
        prefix_dic[elem] = 0
        prefix_set.remove(elem)
    if elem + k in prefix_set:
        ans += prefix_dic[elem + k]
print(ans)
