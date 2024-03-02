n = int(input())
answer = 0
for i in range(1, n + 1):
    if i <= 99:
        answer += 1
    else:
        a, b, c = int(str(i)[0]), int(str(i)[1]), int(str(i)[2])
        if b - a == c - b:
            answer += 1
print(answer)