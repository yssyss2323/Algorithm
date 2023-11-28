n,k = map(int,input().split())
checkdic = {}
for i in range(n):
    a,b= map(int,input().split())
    if (10*b+a) in checkdic:
        checkdic[10*b+a] +=1
    else: checkdic[10*b+a] =1
answer = 0
for i in list(checkdic.values()):
    answer += (i-1)//k+1
print(answer)