from collections import deque

while True:
    m = int(input())
    if m == 0:
        break
    string = input()

    q = deque()
    check = dict()
    ans = 0
    for i in range(len(string)):
        ch = string[i]
        q.append(ch)
        check[ch] = check.get(ch, 0) + 1
        if len(check.keys()) > m:
            trash = q.popleft()
            if check[trash] > 1:
                check[trash] -= 1
            else:
                del check[trash]
        if len(q) > ans:
            ans = len(q)
    print(ans)