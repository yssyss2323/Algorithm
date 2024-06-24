def check(num1, num2, strike, ball):
    cnt = 0
    for i in range(3):
        if num1[i] in num2:
            cnt += 1
    s = 0
    for i in range(3):
        if num1[i] == num2[i]:
            s += 1
    b = cnt - s
    if s == strike and b == ball:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    qna = [input().split() for _ in range(n)]

    table = [False] * 1000
    for i in range(123, 1000):
        tmp = str(i)
        # 숫자야구는 1~9로 함, 서로 다른 숫자여야 함
        if '0' not in str(i) and len(set(tmp)) == 3:
            table[i] = True

    # 모든 세자리 숫자를 대입해서 스트라이크 볼이 일치하는지 체크
    for i in range(n):
        qustion_num = str(qna[i][0])
        for j in range(123, 1000):
            tmp = str(j)
            if check(qustion_num, tmp, int(qna[i][1]), int(qna[i][2])) == False:
                table[j] = False
    print(table.count(True))
