import sys
input = lambda:sys.stdin.readline().rstrip()

check = dict()

while True:
    word = input()
    if not word:
        break
    key = "".join(sorted(word))
    check[key] = check.get(key, []) + [word]

anslist = []
for value in check.values():
    value.sort()
    anslist.append(value)
anslist.sort(key=lambda x: (-len(x), x[0]))

for i in range(min(len(anslist), 5)):
    ans = list(set(anslist[i]))
    ans.sort()
    print(f"Group of size {len(anslist[i])}: ", end="")
    print(*ans, end=" .\n")