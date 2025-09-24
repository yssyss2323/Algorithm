n = int(input())

check = int(input())
questions = [check]
for _ in range(n - 1):
    questions.append(int(input()))

if check == min(questions):
    print("ez")
elif check == max(questions):
    print("hard")
else:
    print("?")