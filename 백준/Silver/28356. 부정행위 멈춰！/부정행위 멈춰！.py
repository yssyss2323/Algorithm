import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
    print(1)
elif n == 1:
    arr = [1, 2] * (m // 2) + [1] * (m % 2)
    print(2)
    print(*arr)
elif m == 1:
    arr = [1, 2] * (n // 2) + [1] * (n % 2)
    print(2)
    print(*arr, sep='\n')
else:
    print(4)
    arr1 = [1, 3] * (m // 2) + [1] * (m % 2)
    arr2 = [2, 4] * (m // 2) + [2] * (m % 2)
    arr = [arr1, arr2] * (n // 2)
    arr.append(arr1 * (n % 2))

    for row in arr:
        print(*row)
