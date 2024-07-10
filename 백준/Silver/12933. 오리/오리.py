sound = input()
q, u, a, c, k = 0, 0, 0, 0, 0

answer = 0
for ch in sound:
    if ch =='q':
        if answer: answer-= 1; q+= 1
        else: q += 1
    elif ch == 'u':
        if q: u += 1; q -= 1
        else: print(-1); break
    elif ch == 'a':
        if u: a += 1; u -= 1
        else: print(-1); break
    elif ch == 'c':
        if a: c+= 1; a -= 1
        else: print(-1); break
    elif ch == 'k':
        if c:
            answer += 1
            c -= 1
        else: print(-1); break
else:
    if q or u or a or c or k:
        print(-1)
    else:
        print(answer)