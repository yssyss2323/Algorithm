def find_case(arr):
    if len(arr) >= 4 and sum(arr) >= 15:
        if sum(arr) == 15:
            tmp = arr[:]
            test_case2.append(tmp)
        return
    for i in 1,2,3,4,5:
        if not arr or arr[-1] <= i:
            arr.append(i)
            find_case(arr)
            arr.pop()

levels_cost = list(map(int, input().split()))
test_case = [[5,5],[3,3,4],[2,3,5],[1,4,5],[2,4,4]]
test_case2 = []
find_case([])
test_case += test_case2

ans = 0
for case in test_case:
    tmp = 0
    for i in case:
        tmp += levels_cost[i - 1]
    if tmp > ans:
        c = case
        ans = tmp
print(ans)