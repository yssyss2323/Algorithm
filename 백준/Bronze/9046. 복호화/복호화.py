t = int(input())
for _ in range(t):
    check = {chr(i):0 for i in range(97,123)}
    tmp = ''
    for string in input().split():
        tmp += string

    ans = []
    stand = 0
    for ch in tmp:
        check[ch] += 1
        if check[ch] > stand:
            stand = check[ch]
            ans = [ch]
        elif check[ch] == stand:
            ans.append(ch)
    if len(ans) > 1:
        print('?')
    else:
        print(ans[0])

