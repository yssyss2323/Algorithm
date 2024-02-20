n = int(input())
dic = {}
for i in range(n):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
answer, tmp = '', 0
for i in sorted(dic.keys()):
    if dic[i] > tmp:
        answer = i
        tmp = dic[i]
print(answer)