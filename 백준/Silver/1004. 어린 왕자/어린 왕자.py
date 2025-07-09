t = int(input())
answer = [0]*t
for testcase in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    starlist = []
    for _ in range(n):
        starlist.append(list(map(int,input().split())))
    for ii in starlist:
        d1 = ((x1-ii[0])**2 + (y1-ii[1])**2)**0.5
        d2 = ((x2-ii[0])**2 + (y2-ii[1])**2)**0.5
        if (d1 < ii[2] and d2> ii[2]) or (d1 > ii[2] and d2 < ii[2]):
            answer[testcase] += 1
for ii in answer:
    print(ii)
