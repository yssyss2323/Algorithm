ans = ""
check = 0

for _ in range(7):
    name, num = input().split()
    if int(num) > check:
        check = int(num)
        ans = name
print(ans)