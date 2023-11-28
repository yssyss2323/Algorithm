n, m = map(int, input().split())
xxmap = [list(input()) for _ in range(n)]
for ii in range(n):
    for jj in range(m):
        if xxmap[ii][jj] == 'O':
            goal = [ii,jj]
        if xxmap[ii][jj] == 'R':
            red = [ii,jj]
            xxmap[ii][jj] = '.'
        if xxmap[ii][jj] =='B':
            blue = [ii,jj]
            xxmap[ii][jj] = '.'

def nextyy(xmap,nowred, nowblue, direction,tag):
    if direction == 'right':
        xmap[nowblue[0]][nowblue[1]] ='B'
        for ii in range(nowred[1]+1,len(xmap[0])):
            if xmap[nowred[0]][ii] != '.':
                if xmap[nowred[0]][ii] == 'O':
                    nowred[1] = ii
                    xmap[nowblue[0]][nowblue[1]] = '.'
                    break
                elif xmap[nowred[0]][ii] == 'B':
                    xmap[nowred[0]][ii] = '.'
                    for jj in range(ii+1,len(xmap[0])):
                        if xmap[nowred[0]][jj] != '.':
                            if xmap[nowred[0]][jj] =='O':
                                nowblue[1] = jj
                                nowred[1] = jj
                            else:
                                nowblue[1] = jj-1
                                nowred[1] = jj-2
                            break
                else:
                    nowred[1] = ii-1
                    xmap[nowblue[0]][nowblue[1]] = '.'
                break
        if nowred != tag:
            xmap[nowred[0]][nowred[1]] = 'R'
        for ii in range(nowblue[1]+1,len(xmap[0])):
            if nowblue == tag:
                break
            if xmap[nowblue[0]][ii] != '.':
                if xmap[nowblue[0]][ii] == 'O':
                    nowblue[1] = ii
                    break
                else:
                    nowblue[1] = ii-1
                break
        if nowred != tag:
            xmap[nowred[0]][nowred[1]] = '.'
    if direction == 'left':
        xmap[nowblue[0]][nowblue[1]] = 'B'
        for ii in reversed(range(0,nowred[1])):
            if xmap[nowred[0]][ii] != '.':
                if xmap[nowred[0]][ii] == 'O':
                    nowred[1] = ii
                    xmap[nowblue[0]][nowblue[1]] = '.'
                elif xmap[nowred[0]][ii] == 'B':
                    xmap[nowred[0]][ii] = '.'
                    for jj in reversed(range(0,ii)):
                        if xmap[nowred[0]][jj] != '.':
                            if xmap[nowred[0]][jj] == 'O':
                                nowblue[1] = jj
                                nowred[1] = jj
                            else:
                                nowblue[1] = jj + 1
                                nowred[1] = jj + 2
                            break
                else:
                    xmap[nowblue[0]][nowblue[1]] = '.'
                    nowred[1] = ii + 1
                break
        if nowred != tag:
            xmap[nowred[0]][nowred[1]] = 'R'
        for ii in reversed(range(0,nowblue[1])):
            if nowblue == tag:
                break
            if xmap[nowblue[0]][ii] != '.':
                if xmap[nowblue[0]][ii] == 'O':
                    nowblue[1] = ii
                    break
                else:
                    nowblue[1] = ii + 1
                break
        if nowred != tag:
            xmap[nowred[0]][nowred[1]] = '.'
    if direction == 'down':
        tmpmap = [[0 for _ in range(len(xmap))] for _ in range(len(xmap[0]))]
        for ii in range(len(xmap)):
            for jj in range(len(xmap[0])):
                tmpmap[jj][ii] = xmap[ii][jj]
        tmpred, tmpblue, tmptag = [nowred[1],nowred[0]], [nowblue[1],nowblue[0]], [tag[1],tag[0]]
        nextyy(tmpmap,tmpred,tmpblue,'right',tmptag)
        nowred,nowblue = [tmpred[1],tmpred[0]],[tmpblue[1],tmpblue[0]]
    if direction =='up':
        tmpmap = [[0 for _ in range(len(xmap))] for _ in range(len(xmap[0]))]
        for ii in range(len(xmap)):
            for jj in range(len(xmap[0])):
                tmpmap[jj][ii] = xmap[ii][jj]
        tmpred, tmpblue, tmptag = [nowred[1], nowred[0]], [nowblue[1], nowblue[0]], [tag[1],tag[0]]
        nextyy(tmpmap, tmpred, tmpblue, 'left',tmptag)
        nowred, nowblue = [tmpred[1], tmpred[0]], [tmpblue[1], tmpblue[0]]
    return nowred,nowblue


directlist = ['right', 'left', 'up', 'down']
visited = []
answer = -1
answerqueue = [[red,blue,1]]
while answerqueue :
    realred,realblue,idx = answerqueue.pop(0)
    visited.append(realred+realblue)
    for ii in range(4):
        xxx = list(realred)
        yyy = list(realblue)
        tmp2 = nextyy(xxmap, xxx, yyy, directlist[ii],goal)
        newred = tmp2[0]
        newblue = tmp2[1]
        if newred+newblue in visited:
            continue
        else:
            if newblue == goal:
                continue
            elif newred == goal:
                answer = idx
                answerqueue = []
                break
            else:
                newidx = idx +1
                if newidx <= 10:
                    answerqueue.append([newred,newblue,newidx])
print(answer)