n = int(input())
numlist = list(map(int,input().split()))
numlist.sort()
x = int(input())
start, end = 0 , len(numlist)-1
answer = 0
while start < end:
    if numlist[start] + numlist[end] == x:
        answer += 1
        start +=1
        end += -1
    elif numlist[start] + numlist[end] < x:
        start += 1
    else:
        end += -1
print(answer)