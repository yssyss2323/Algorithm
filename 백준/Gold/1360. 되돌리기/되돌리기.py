n = int(input())
orderlist, chrlist, seclist = [], [], []
for _ in range(n):
    order, ch, sec = input().split()
    orderlist.append(order)
    chrlist.append(ch)
    seclist.append(sec)
orderlist.reverse()
chrlist.reverse()
seclist.reverse()

answer = ''
for i in range(n):
    if orderlist[i] == 'undo':
        endsec = int(seclist[i])
        startsec = endsec - int(chrlist[i])
        for j in range(i, n):
            if startsec <= int(seclist[j]) <= endsec:
                x = j
        for k in range(i, x + 1):
            orderlist[k] = ''
            chrlist[k] = ''
            seclist[k] = ''
    if orderlist[i] == 'type':
        answer = chrlist[i] + answer
print(answer)
