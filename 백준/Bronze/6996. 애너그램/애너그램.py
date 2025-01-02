n = int(input())
for _ in range(n):
    a, b = input().split()
    check = ' '
    if sorted(a) != sorted(b):
        check = ' NOT '
    print(f"{a} & {b} are{check}anagrams.")