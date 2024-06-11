T = int(input())
for _ in range(T):
    n = int(input())
    fashion_dic = dict()
    for _ in range(n):
        _, type = input().split()
        fashion_dic[type] = fashion_dic.get(type, 0) + 1
    ans = 1
    for key in fashion_dic.keys():
        ans *= (fashion_dic[key] + 1)
    print(ans - 1)
