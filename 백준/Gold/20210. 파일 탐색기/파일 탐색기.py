from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

eng_dic1 = {chr(i): i * 2 - 129 for i in range(65, 91)}
eng_dic2 = {chr(i): i * 2 - 192 for i in range(97, 123)}

words = []
max_num = 10 ** 103
for _ in range(int(input())):
    word = deque(input())
    tmp = []
    while word:
        ch = word.popleft()
        if ch in [chr(i) for i in range(65, 91)]:
            tmp.append(max_num + eng_dic1[ch])
        elif ch in [chr(i) for i in range(97, 123)]:
            tmp.append(max_num + eng_dic2[ch])
        else:
            tmp_num = int(ch)
            cnt_zero = 0
            if tmp_num == 0:
                cnt_zero = 1
                while word and word[0] == '0':
                    word.popleft()
                    cnt_zero += 1
            while word and word[0] in '1234567890':
                tmp_num *= 10
                n = int(word.popleft())
                tmp_num += int(n)
            tmp_num *= 1000
            if cnt_zero > 0:
                tmp_num += cnt_zero
            tmp.append(tmp_num)
    words.append(tmp)

words.sort()
for word in words:
    ans = ''
    for n in word:
        if max_num < n:
            n -= max_num
            if n % 2:
                ans += chr(65 + (n - 1) // 2)
            else:
                ans += chr(96 + n // 2)
        else:
            if n % 1000:
                ans += '0' * (n % 1000)
            if n // 1000:
                ans += str(n // 1000)
    print(ans)