def find_factor(x):
    arr = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i:
            continue
        else:
            arr.append(i)
            while x % i == 0:
                x //= i
    if x > 1:
        arr.append(x)
    return arr

while True:
    num = int(input())
    if num == 0:
        break
    elif num == 1:
        print(0)
    else:
        factor = find_factor(num)
        for i in factor:
            num *= i - 1
            num //= i
        print(num)
