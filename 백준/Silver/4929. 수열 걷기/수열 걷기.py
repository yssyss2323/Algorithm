while True:
    arr = list(map(int, input().split()))
    n1, s1 = arr[0], arr[1:]
    if n1 == 0:
        break
    arr = list(map(int, input().split()))
    n2, s2 = arr[0], arr[1:]
    commons = sorted(set(s1).intersection(set(s2)))

    ans = 0
    idx1, idx2 = 0, 0
    for n in commons:
        n1 = s1.index(n)
        tmp_s1 = sum(s1[idx1:n1])
        n2 = s2.index(n)
        tmp_s2 = sum(s2[idx2:n2])
        ans += max(tmp_s1, tmp_s2) + n
        idx1 = n1 + 1
        idx2 = n2 + 1
    ans += max(sum(s1[idx1:]), sum(s2[idx2:]))
    print(ans)