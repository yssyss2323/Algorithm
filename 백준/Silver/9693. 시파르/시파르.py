i = 0
while True:
    i += 1
    n = int(input())
    if n == 0:
        break

    ans = 0
    while n > 0:
        n //= 5
        ans += n
    print(f"Case #{i}: {ans}")
