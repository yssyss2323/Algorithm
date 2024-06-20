characters = input()
secrets = input()
n = len(characters)  # n진법으로 생각할 수 있음

check = dict()  # O(1)로 인덱싱해야 시간복잡도 충족
for i in range(n):
    check[characters[i]] = i + 1

ans = 0
for ch in secrets:
    ans *= n
    ans += check[ch]
    ans %= 900528
print(ans)
