check = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
s = input()
ans = 0
for ch in s:
    ans += check[ord(ch)-65]
print("I'm a winner!" if ans % 2 else "You're the winner?")