n = int(input())
plist = list(map(int, input().split()))

for i in range(1, n):
    for j in range((i + 1) // 2):
        if plist[i] < plist[i - j - 1] + plist[j]:
            plist[i] = plist[i - j - 1] + plist[j]
print(plist[-1])