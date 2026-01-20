def print_star(n):
    for i in range(1, n + 1):
        print("*" * i)

while True:
    n = int(input())
    if n == 0:
        break
    print_star(n)