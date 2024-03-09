n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
m = int(input())
mlist = list(map(int, input().split()))

def search(x):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        check = nlist[mid]
        if check == x:
            return 1
        elif check < x:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return 0

for i in mlist:
    print(search(i))
