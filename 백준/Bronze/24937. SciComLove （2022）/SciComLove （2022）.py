str = "SciComLove"
n = int(input()) % len(str)
for _ in range(n):
    str = str[1:] + str[0]
print(str)
