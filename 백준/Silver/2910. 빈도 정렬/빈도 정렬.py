n, c = map(int, input().split())
arr = list(map(int, input().split()))

dic = {i:arr.count(i) for i in arr}
arr = list(dic.keys())
arr.sort(key=lambda x:-dic[x])
for x in arr:
    for _ in range(dic[x]):
        print(x, end= ' ')