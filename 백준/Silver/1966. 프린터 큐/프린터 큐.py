def find_last(arr, x):
    return len(arr) - 1 - arr[::-1].index(x)

for _ in range(int(input())):
    n, m = map(int, input().split())
    print_que = list(map(int, input().split()))
    wanted = print_que[m]
    answer = 0
    for i in reversed(range(wanted + 1, 10)):
        if i in print_que:
            answer += print_que.count(i)
            idx = find_last(print_que, i)
            m = m - idx if m > idx else n + m - idx
            print_que = print_que[idx:] + print_que[:idx]
    answer += print_que[:m + 1].count(wanted)
    print(answer)
