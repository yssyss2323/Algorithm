N, K = map(int, input().split())
numlist = list(range(1, N + 1))
answerlist = []
while numlist:
    tmp = (K - 1) % len(numlist)
    answerlist.append(str(numlist[tmp]))
    numlist = numlist[tmp + 1:] + numlist[:tmp]
print(f"<{', '.join(answerlist)}>")