import sys
input = sys.stdin.readline

check = list(map(str, range(10))) + ["A", "B", "C", "D", "E", "F"]

def transform(num, x):
    ans = ""
    while num:
        ans += check[num % x]
        num = num // x
    return ans[::-1] == ans


for _ in range(int(input())):
    a, n = map(int, input().split())
    print(1 if transform(a, n) else 0)