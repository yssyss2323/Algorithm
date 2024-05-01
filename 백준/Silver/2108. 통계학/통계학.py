from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numlist = []
for _ in range(N):
    numlist.append(int(input()))
numlist.sort()
cnt = Counter(numlist)
cnt_most = cnt.most_common(2)
if len(cnt_most) == 1 or cnt_most[0][1] != cnt_most[1][1]:
    most_freq = cnt_most[0][0]
else:
    most_freq = cnt_most[1][0]
print(round(sum(numlist) / N))
print(numlist[N // 2])
print(most_freq)
print(numlist[-1] - numlist[0])
