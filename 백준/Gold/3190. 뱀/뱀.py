N = int(input())
k = int(input())
apples = [list(map(int,input().split())) for _ in range(k)]
L = int(input())
changes = [input().split() for _ in range(L)]
dic_change ={}
for ii in changes:
    dic_change[int(ii[0])] = 1 if ii[1] == 'D' else -1
gamemap = [[False for _ in range(N+2)]] + [[False] + [True for _ in range(N)] + [False] for _ in range(N)] + [[False for _ in range(N+2)]]
for ii in apples:
    gamemap[ii[0]][ii[1]] = 'apple'
head = [1,1]
gamemap[head[0]][head[1]] = False
body = []
body.append(head)
currenttime = 0
directnum = 0
directlist = ['right','down','left','up']
xmove = [0,1,0,-1]
ymove = [1,0,-1,0]

while True:
    nexttime = currenttime + 1
    if currenttime in dic_change.keys():
        directnum += dic_change[currenttime]
        directnum %= 4
    currentdirect = directlist[directnum]
    nexthead = [head[0]+xmove[directnum],head[1]+ymove[directnum]]
    currenttime = nexttime

    if gamemap[nexthead[0]][nexthead[1]] == True:
        body.append(nexthead[:])
        gamemap[nexthead[0]][nexthead[1]] = False
        tmp = body.pop(0)
        gamemap[tmp[0]][tmp[1]] = True
        head = nexthead[:]
    else:
        if gamemap[nexthead[0]][nexthead[1]] == 'apple':
            gamemap[nexthead[0]][nexthead[1]] = False
            body.append(nexthead[:])
            head = nexthead[:]
        else:
            break
print(currenttime)