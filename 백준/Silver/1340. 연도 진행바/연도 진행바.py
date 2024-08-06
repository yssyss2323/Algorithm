n = list(input().split())
n.append('')
n[1] = n[1][:2]
n[3],n[4] = n[3].split(':')

month = ['x','January','February','March','April','May','June','July','August','September','October','November','December']
monthday = [0,31,28,31,30,31,30,31,31,30,31,30,31]

yoonday = 0
if int(n[2]) % 400 == 0 or (int(n[2])%100 != 0 and int(n[2])%4 ==0):
    yoonday = 1
monthday[2] += yoonday

totalmin = sum(monthday)*24*60
nowmin = (sum(monthday[:month.index(n[0])])+int(n[1])-1)*24*60 + int(n[3])*60 + int(n[4])

print(nowmin*100/totalmin)
