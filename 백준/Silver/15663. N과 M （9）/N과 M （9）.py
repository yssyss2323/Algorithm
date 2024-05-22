def bt(given, arr, n, m):
    if len(arr) == m:
        tmparr = tuple(arr)
        if tmparr not in answers:
            answers.add(tmparr)
        return

    for i in range(n):
        tmp = given[i]
        if tmp == 0:
            continue
        given2 = given[:i] + [0] + given[i+1:]
        arr.append(tmp)
        bt(given2, arr, n, m)
        arr.pop()


N, M = map(int, input().split())
given_arr = list(map(int, input().split()))
given_arr.sort()
answers = set()

bt(given_arr, [], N, M)
for answer in sorted(answers):
    print(*answer)