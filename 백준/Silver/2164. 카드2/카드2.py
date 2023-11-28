N = int(input())
answerlist = [1] * N
# 카드가 n개일때의 출력을 answerlist[n-1]에 저장
for i in range(1, N):
    if answerlist[i-1] == i:
        answerlist[i] = 2
    else:
        answerlist[i] = answerlist[i-1] + 2
print(answerlist[-1])