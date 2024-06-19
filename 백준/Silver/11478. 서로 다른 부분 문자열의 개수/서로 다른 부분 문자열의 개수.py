string = input()
n = len(string)
check = set()
for i in range(1, n + 1):
    for j in range(n - i + 1):
        check.add(string[j:j + i])
print(len(check))