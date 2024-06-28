def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    global cnt,k
    i = start
    j = mid + 1
    tmp = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    while j <= end:
        tmp.append(arr[j])
        j += 1

    for t in range(start, end + 1):
        #print(arr, tmp[t-start])
        arr[t] = tmp[t - start]
        cnt += 1
        if cnt == k:
            print(arr[t])
            exit()


n,k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
merge_sort(arr, 0, n - 1)
print(-1)
