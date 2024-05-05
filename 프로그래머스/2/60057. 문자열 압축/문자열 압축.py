# 문자열을 n개씩 토큰화시키는 함수
def token_of_string(given_string, n):
    num_of_token = (len(given_string) - 1) // n + 1
    tokens = []
    for _ in range(num_of_token):
        tokens.append(given_string[:n])
        given_string = given_string[n:]
    tokens.append('0')
    return tokens

# 문자열을 n개 단위로 압축시키는 함수
def compression_of_string(given_string, n):
    tokens = token_of_string(given_string, n)
    compressed_string = ""
    now, check = 0, 0 # check는 반복문 탈출을 위한 변수입니다
    while True:
        cnt = 1 # 연속하는 동일한 토큰의 개수를 카운트하는 변수입니다
        for i in range(now + 1, len(tokens)):
            check = i
            if tokens[now] == tokens[i]:
                cnt += 1
            else:
                break
        # 압축 문자열을 만드는 과정입니다
        if cnt > 1:
            compressed_string += f"{cnt}{tokens[now]}"
        else:
            compressed_string += f"{tokens[now]}"

        if check == len(tokens) - 1:
            break
        now = check
    return compressed_string

# 정답 구하는 함수
def solution(s):
    if len(s) == 1:
        answer = 1
    else:
        answer = float("inf")
        for token_length in range(1, len(s) // 2 + 1):
            tmp_string = compression_of_string(s, token_length)
            answer = min(answer, len(tmp_string))
    return answer