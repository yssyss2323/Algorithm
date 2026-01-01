def check(string):
    if len(string) % 2:
        return string

    prev_string = ""
    for i in range(len(string) // 2 - 1):
        if string[i * 2 + 1] == string[i * 2 + 3]:
            return string
        else:
            prev_string += int(string[i * 2]) * string[i * 2 + 1]
    else:
        prev_string += int(string[-2]) * string[-1]
        if string == prev_string:
            return string
        return check(prev_string)


cnt = 1
while True:
    curr = input()
    if curr == '0':
        break
    print(f"Test {cnt}: {check(curr)}")
    cnt += 1