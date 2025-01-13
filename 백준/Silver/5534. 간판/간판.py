def check(key, word):
    length = len(key)
    gap = 1
    while length <= len(word):
        tmp = word[:length:gap]
        if tmp == key:
            return True
        length += len(key) - 1
        gap += 1
    return False


n = int(input())
key = input()
ans = 0
for _ in range(n):
    val = input()
    for i in range(len(val)):
        ch = val[i]
        if ch == key[0] and check(key, val[i:]):
            ans += 1
            break
print(ans)