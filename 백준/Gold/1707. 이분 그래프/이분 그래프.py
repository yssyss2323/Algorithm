import sys
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)

    check = [0 for _ in range(V + 1)]
    for i in range(1, V + 1):
        if check[i] == 0:
            stack = [i]
            check[i] = 1
            flag = False
            while stack:
                curr = stack.pop()
                nex = arr[curr]
                for x in nex:
                    if check[x] == 0:
                        stack.append(x)
                        check[x] = -check[curr]
                    else:
                        if check[x] == check[curr]:
                            flag = True
                            break
            if flag:
                print("NO")
                break
    else:
        print("YES")
