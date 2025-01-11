words = set()
for _ in range(int(input())):
    curr = input()
    words.add(curr)
    if curr[::-1] in words:
        print(len(curr), curr[len(curr) // 2])
        break