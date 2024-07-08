while True:
    password = input()
    if password == 'end':
        break
    length = len(password)
    ans = ''
    if length == 1:
        if password not in 'aeiou':
            ans = 'not ' # 길이1인데 자음인 경우
    elif length == 2:
        if password[0] not in 'aeiou' and password[1] not in 'aeiou':
            ans = 'not ' # 길이2인데 둘다 자음인 경우
        elif password[0] == password[1]:
            if password[0] not in 'eo':
                ans = 'not ' # 길이2인데 동일글자 (ee, oo 제외)
    else:
        prev = password[0] in 'aeiou'
        risk = False
        for i in range(1, len(password) - 1):
            check = password[i] in 'aeiou'
            risk = prev == check
            if risk: # 지금문자랑 이전문자가 연속자음 or 연속모음일때
                if check == (password[i+1] in 'aeiou'):
                    ans = 'not ' # 3연속 자음 or 3연속 모음
                    break
            prev = check
            if password[i-1] == password[i]:
                if password[i] not in 'eo':
                    ans = 'not ' # 동일글자 (ee, oo 제외)
                    break
        else:
            if password[-2] == password[-1]: # 맨 마지막글자 동일글자여부 체크
                if password[-1] not in 'eo':
                    ans = 'not '
    print(f"<{password}> is {ans}acceptable.")