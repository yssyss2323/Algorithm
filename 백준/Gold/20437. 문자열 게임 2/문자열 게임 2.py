import sys
input = lambda:sys.stdin.readline().rstrip()


for _ in range(int(input())):
    alphabet = {chr(i): [] for i in range(ord('a'), ord('z') + 1)}
    w = input()
    k = int(input())

    for i in range(len(w)):
        ch = w[i]
        alphabet[ch].append(i)

    ans = []
    for i in range(ord('a'), ord('z') + 1):
        ch = chr(i)
        length = len(alphabet[ch])
        if length >= k:
            for j in range(length - k + 1):
                tmp = alphabet[ch][j + k - 1] - alphabet[ch][j]
                ans.append(tmp + 1)
    if ans:
        ans.sort()
        print(ans[0], ans[-1])
    else:
        print(-1)