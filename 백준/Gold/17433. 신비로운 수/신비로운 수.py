import sys
input = sys.stdin.readline

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

for _ in range(int(input())):

    n = int(input())
    if n == 1:
        print("INFINITY")
    else:
        nums = list(map(int, input().split()))
        nums.sort()
        gaps = [nums[i + 1] - nums[i] for i in range(n - 1)]

        if len(gaps) == 1:
            print(gaps[0])
        else:
            ans = gaps.pop()
            for gap in gaps:
                ans = gcd(ans, gap)
            if ans == 0:
                print("INFINITY")
            else:
                print(ans)