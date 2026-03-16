for _ in range(int(input())):
    n = int(input())
    nums = set(map(int, input().split()))
    m = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        print(1 if i in nums else 0)