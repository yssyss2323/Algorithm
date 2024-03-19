name = input()
engdic = {}
even = [0] * 26
odd = []
for i in range(26):
    if chr(i + 65) in name:
        cnt = name.count(chr(i + 65))
        if cnt % 2 == 0:
            even[i] = cnt
        else:
            even[i] = cnt - 1
            odd.append(chr(i + 65))

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    answer = ""
    for i in range(26):
        for j in range(even[i] // 2):
            answer += chr(i + 65)
    if odd:
        answer += odd[-1]
    for i in reversed(range(26)):
        for j in range(even[i] // 2):
            answer += chr(i + 65)
    print(answer)