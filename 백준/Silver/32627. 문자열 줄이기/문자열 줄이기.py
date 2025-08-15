n, m = map(int, input().split())
s = input()
if m == 0:
    print(s)
else:
    idx_set = set()
    flag = False
    for i in range(ord('a'), ord('z') + 1):
        for j in range(n):
            if s[j] == chr(i):
                idx_set.add(j)
                m -= 1
                if m == 0:
                    flag = True
                    break
        if flag:
            break

    idx_list = list(set(range(n)).difference(idx_set))
    idx_list.sort()
    ans = [s[i] for i in idx_list]
    print(*ans, sep='')