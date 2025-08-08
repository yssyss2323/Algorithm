import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        arr = [int(input()) for _ in range(n)]
        arr.sort()
        l, r = 0, n - 1
        while l < r:
            if arr[l] + arr[r] == x:
                print(f"yes {arr[l]} {arr[r]}")
                break
            elif arr[l] + arr[r] > x:
                r -= 1
            else:
                l += 1
        else:
            print("danger")
    except:
        break