n = int(input())
arr = list(input().split())
arr_origin = arr[:]
check = {'B':0, 'S':1, 'G':2, 'P':3, 'D':4}
arr.sort(key=lambda x: (check[x[0]], -int(x[1:])))

ans = []
for i in range(n):
    if arr[i] != arr_origin[i]:
        print("KO")
        print(arr[i], arr_origin[i])
        break
else:
    print("OK")
