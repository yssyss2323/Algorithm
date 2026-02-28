string = input()
stack = []

for ch in string:
    stack.append(ch)
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()
if stack == ['P']:
    print("PPAP")
else:
    print("NP")