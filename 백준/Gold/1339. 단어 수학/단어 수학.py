N = int(input())
position = [0] * 26
for _ in range(N):
    word = input()
    for i in range(len(word)):
        position[ord(word[i]) - ord('A')] += 10 ** (len(word) - i -1)

arr = []
for value in position:
    if value:
        arr.append(value)
arr.sort()

answer = 0
for i in range(len(arr)):
    answer += arr[i] * (10 - len(arr) + i)
print(answer)