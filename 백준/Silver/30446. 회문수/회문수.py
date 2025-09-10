n = input()

ans = 0
for i in range(len(n)- 1):
    ans += 9 * (10 ** (i // 2))

half_start = 10 ** ((len(n) - 1) // 2)
half_end = n[:(len(n) - 1) // 2 + 1]
half_check = half_end[::-1]
if len(n) % 2:
    half_check = half_check[1:]
check = int(half_end + half_check)
if check > int(n):
    half_end = int(half_end) - 1
else:
    half_end = int(half_end)
ans += half_end - half_start + 1
print(ans)