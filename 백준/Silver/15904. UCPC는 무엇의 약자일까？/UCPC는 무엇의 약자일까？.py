string = input()

check = "UCPC"
curr = 0
for ch in string:
    if ch == check[curr]:
        curr += 1
    if curr == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")