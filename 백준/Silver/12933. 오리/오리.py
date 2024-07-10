sound = input()
q, u, a, c, k = 0, 0, 0, 0, 0
qq, uu, aa, cc, kk = 0, 0, 0, 0, 0

ans, save = 0, 0
for ch in sound:
    if ch =='q':
        if save: save-= 1; q+= 1 #; qq += 1
        else: q += 1
    elif ch == 'u':
        if q: u += 1; q -= 1
        # elif qq: uu += 1; qq -= 1
        else: print(-1); break
    elif ch == 'a':
        if u: a += 1; u -= 1
        # elif uu: aa += 1; uu -= 1
        else: print(-1); break
    elif ch == 'c':
        if a: c+= 1; a -= 1
        # elif aa: cc+= 1; aa -= 1
        else: print(-1); break
    elif ch == 'k':
        if c:
            save += 1
            c -= 1
            #ans += 1; save += 1; c -= 1
        # elif cc: save += 1; cc -= 1
        else: print(-1); break
    # print(q,u,a,c,k,' ', save, ans)
else:
    if q or u or a or c or k: #or qq or uu or aa or cc or kk:
        print(-1)
    else:
        print(save)