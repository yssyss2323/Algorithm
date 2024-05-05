def solution(s):
    answer = len(s)

    for i in range(1,int(len(s)/2)+1): #range함수 특성상 종료값이 포함되지 않기때문에 포함시키기 위해 +1해줌
        pos = 0 #어느 위치에서 처리중인지 표현하는 포지션 변수
        length  = len(s) #처음엔 문자열 길이로 초기화. 후에 압축된 길이로 바꿔줄거임.

        while pos + i <= len(s):
            unit = s[pos:pos+i]
            pos += i #진행된 만큼 포지션에 반영

            cnt = 1
            while pos + i <= len(s):
                test = s[pos:pos+i]
                if unit == s[pos:pos+i]:
                    cnt += 1
                    pos += i
                else:
                    break

            if cnt > 1: #압축이 됐다면
                length -= i*(cnt - 1)
                length += len(str(cnt))



        answer = min(answer, length)

    return answer