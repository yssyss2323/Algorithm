n, k = map(int, input().split())
string = input()

ans = ""
for i in range(n - 1):
    if string[i] == "A":
        ans += "A"
        continue
    tmp = ord('Z') - ord(string[i])
    if k > tmp:
        ans += "A"
        k -= tmp + 1
    else:
        ans += string[i]
ans += chr((ord(string[n - 1]) + k - ord("A")) % 26 + ord("A"))
print(ans)
