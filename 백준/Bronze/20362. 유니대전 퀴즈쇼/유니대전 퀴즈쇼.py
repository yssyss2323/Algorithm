import sys
input = sys.stdin.readline

n, s = input().split()
arr = [list(input().split()) for _ in range(int(n))]

check = ""
ans = 0
for word, chat in reversed(arr):
    if word == s:
        check = chat
        continue
    if check and chat == check:
        ans += 1
print(ans)