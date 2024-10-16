doc = input()
target = input()

ans = 0
while True:
    length = len(target)
    curr = doc.find(target)
    if curr == -1:
        break
    else:
        ans += 1
        doc = doc[curr + length:]
print(ans)