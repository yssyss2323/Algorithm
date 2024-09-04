n = input()
ans = int(n[-1])
for i in range(len(n) - 2, -1, -1):
    if n[i + 1] == '0':
        ans += int(n[i]) * 10
    else:
        ans += int(n[i])
print(ans)