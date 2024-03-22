c,n = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
answerlist = [float('inf')] * (c + 100)
answerlist[0] = 0
for i in range(n):
    cost, num = arr[i][0], arr[i][1]
    for j in range(num,len(answerlist)):
        answerlist[j] = min(answerlist[j-num]+cost, answerlist[j])
print(min(answerlist[c:]))