ans = []
for i in range(5):
    s = input()
    if "FBI" in s:
        ans.append(i + 1)
if ans:
    print(*ans)
else:
    print("HE GOT AWAY!")