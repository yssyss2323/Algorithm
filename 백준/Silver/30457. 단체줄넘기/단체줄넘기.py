n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

left, right = [0], [0]
cnt = 0
while arr:
    curr = arr.pop()
    if left[-1] > right[-1]:
        if right[-1] < curr:
            right.append(curr)
            cnt += 1
        else:
            continue
    else:
        if left[-1] < curr:
            left.append(curr)
            cnt += 1
        else:
            continue
print(cnt)
