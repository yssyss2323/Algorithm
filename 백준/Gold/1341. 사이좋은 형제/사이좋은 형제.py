a,b = map(int,input().split())

for i in range(1, 61):
    if (2**i - 1) % b == 0:
        factor = (2**i - 1) // b
        break
else:
    print(-1)
    exit()
    
abin, bbin = bin(a*factor)[2:], bin(b*factor)[2:]
if len(abin) < len(bbin):
    abin = '0' * (len(bbin) - len(abin)) + abin
for i in abin:
    print('*' if i == '1' else '-', end='')