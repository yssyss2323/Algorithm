n = int(input())
xxmap = [list(map(int, input().split())) for _ in range(n)]
dirlist = ['e', 'w', 's', 'n']
answer = 0
maxnum = set()

def dir(xmap, action):
    copymap = [row[:] for row in xmap]
    if action == 'e':
        for ii in range(len(copymap)):
            tmp1 = copymap[ii].count(0)
            if tmp1 == len(copymap[ii]):
                continue
            tmplist1 = [0 for _ in range(tmp1)]
            tmplist2 = []
            for jj in range(len(copymap[ii])):
                if copymap[ii][jj] != 0:
                    tmplist2.append(copymap[ii][jj])
            copymap[ii] = tmplist1 + tmplist2
            for jj in reversed(range(len(copymap[ii]) - 1)):
                if copymap[ii][jj] == copymap[ii][jj + 1]:
                    copymap[ii][jj] = 0
                    copymap[ii][jj + 1] *= 2
            tmp2 = copymap[ii].count(0)
            tmplist3 = [0 for _ in range(tmp2)]
            tmplist4 = []
            for jj in range(len(copymap[ii])):
                if copymap[ii][jj] != 0:
                    tmplist4.append(copymap[ii][jj])
            copymap[ii] = tmplist3 + tmplist4
    if action == 'w':
        for ii in range(len(copymap)):
            tmp1 = copymap[ii].count(0)
            if tmp1 == len(copymap[ii]):
                continue
            tmplist1 = [0 for _ in range(tmp1)]
            tmplist2 = []
            for jj in range(len(copymap[ii])):
                if copymap[ii][jj] != 0:
                    tmplist2.append(copymap[ii][jj])
            copymap[ii] = tmplist2 + tmplist1
            for jj in range(len(copymap[ii]) - 1):
                if copymap[ii][jj] == copymap[ii][jj + 1]:
                    copymap[ii][jj] *= 2
                    copymap[ii][jj + 1] = 0
            tmp2 = copymap[ii].count(0)
            tmplist3 = [0 for _ in range(tmp2)]
            tmplist4 = []
            for jj in range(len(copymap[ii])):
                if copymap[ii][jj] != 0:
                    tmplist4.append(copymap[ii][jj])
            copymap[ii] = tmplist4 + tmplist3
    if action == 's':
        tmpmap1 = []
        for jj in range(len(copymap[0])):
            tmplist = []
            for ii in copymap:
                tmplist.append(ii[jj])
            tmpmap1.append(tmplist)
        tmpmap2 = dir(tmpmap1,'e')
        copymap = [[tmpmap2[j][i] for j in range(len(tmpmap2))] for i in range(len(tmpmap2[0]))]
    if action == 'n':
        tmpmap1 = []
        for jj in range(len(copymap[0])):
            tmplist = []
            for ii in copymap:
                tmplist.append(ii[jj])
            tmpmap1.append(tmplist)
        tmpmap2 = dir(tmpmap1, 'w')
        copymap = [[tmpmap2[j][i] for j in range(len(tmpmap2))] for i in range(len(tmpmap2[0]))]
    return copymap



def dfs(xmap,idx):
    global maxnum
    if idx == 5 :
        tmp = []
        for ii in xmap:
            tmp.append(max(ii))
        maxnum.add(max(tmp))
        return
    for ii in range(4):
        dfs(dir(xmap,dirlist[ii]),idx+1)


dfs(xxmap,0)
answer = max(maxnum)
print(answer)
