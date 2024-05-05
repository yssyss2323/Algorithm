def token_of_string(given_string, n):
    num_of_token = (len(given_string) - 1) // n + 1
    tokens = []
    for _ in range(num_of_token):
        tokens.append(given_string[:n])
        given_string = given_string[n:]
    tokens.append('0')
    return tokens

def compression_of_string(given_string, n):
    tokens = token_of_string(given_string, n)
    compressed_string = ""
    now = 0
    while True:
        cnt = 1
        check = 0
        for i in range(now + 1, len(tokens)):
            check = i

            if tokens[now] == tokens[i]:
                cnt += 1
            else:
                break

        if cnt > 1:
            compressed_string += f"{cnt}" + f"{tokens[now]}"
        else:
            compressed_string += f"{tokens[now]}"


        now = check
        if now == len(tokens) - 1:
            break

    return compressed_string

def solution(s):
    if len(s) == 1:
        answer = 1
    else:
        answer = float("inf")
        for token_length in range(1, len(s)):
            tmp_string = compression_of_string(s, token_length)
            answer = min(answer, len(tmp_string))
    return answer