N = int(input())
A = list(map(int, input().split()))
top4 = [0,0,0,0]
possible = True
for a in A:
    for i in range(4):
        if a > top4[i]:
            top4[i] = a
            break
    else:
        possible = False

    if not possible:
        print('NO')
        break
else:
    print('YES')