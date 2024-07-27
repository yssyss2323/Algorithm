n = int(input())
bars = list(map(int, input().split()))
bars.sort()

for i in range(n - 2):
    if bars[i] + bars[i + 1] > bars[i + 2]:
        print('possible')
        break
else:
    print('impossible')
