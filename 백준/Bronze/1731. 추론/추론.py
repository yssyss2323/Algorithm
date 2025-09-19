arr = [int(input()) for _ in range(int(input()))]
if arr[1] - arr[0] == arr[2] - arr[1]:
    print(arr[-1] + arr[1] - arr[0])
else:
    print(arr[-1] * (arr[1] // arr[0]))