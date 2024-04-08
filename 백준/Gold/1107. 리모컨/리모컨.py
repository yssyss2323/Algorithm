def bigger_num(x):
    for i in possible_num:
        if i > x:
            return i
    else:
        return

def smaller_num(x):
    for i in reversed(possible_num):
        if i < x:
            return i
    else:
        return

def find_big(xlist):
    for i in range(len(xlist)):
        if xlist[i] in cracked_num:
            check = i
            break
    else:
        return xlist
    for i in reversed(range(check + 1)):
        if bigger_num(xlist[i]):
            big = xlist[:i] + [bigger_num(xlist[i])] + [min_num] * (len(xlist) - i - 1)
            return big
    else:
        if possible_num[-1] == 0:
            return []
        else:
            first = min_num if min_num else min(possible_num[1:])
            big = [first] + [min_num] * len(xlist)
            return big
            
def find_small(xlist):
    for i in range(len(xlist)):
        if xlist[i] in cracked_num:
            check = i
            break
    else:
        return xlist
    for i in reversed(range(check + 1)):
        if smaller_num(xlist[i]) != None:
            small = xlist[:i] + [smaller_num(xlist[i])] + [max_num] * (len(xlist) - i - 1)
            return small
    else:
        if max_num and len(xlist) > 1:
            small = [max_num] * (len(xlist) - 1)
            return small
        else:
            return []

def list_to_num(xlist):
    tmp = ""
    for i in xlist:
        tmp += str(i)
    return int(tmp)

n = int(input())
m = int(input())
cracked_num = []
if m:
    cracked_num = list(map(int,input().split()))
possible_num = []
for i in range(10):
    if i not in cracked_num:
        possible_num.append(i)

answer = abs(100-n)
if possible_num:
    max_num, min_num = max(possible_num), min(possible_num)
    nlist = list(map(int,str(n)))
    biglist, smalllist = find_big(nlist), find_small(nlist)
    if biglist:
        big = list_to_num(biglist)
        answer = min(answer,abs(big-n)+len(str(big)))
    if smalllist:
        small = list_to_num(smalllist)
        answer = min(answer,abs(small-n)+len(str(small)))
print(answer)