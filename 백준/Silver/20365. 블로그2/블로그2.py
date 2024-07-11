n = int(input())
nstring = [True if i == 'R' else False for i in input()]
nstring.append(nstring[0])
l, r = 0, n
ans = 1
while True:
    #print(l,r, ans)
    cur_color = nstring[l]
    while nstring[l] == cur_color and l < n:
        l += 1
    while nstring[r] == cur_color and r > 0:
        r -= 1
    if l > r:
        break
    ans += 1
print(ans)