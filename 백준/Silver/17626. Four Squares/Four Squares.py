n = int(input())

squares = [i ** 2 for i in range(1, int(n ** 0.5 + 1))]
two_squares = set([i + j for i in squares for j in squares])
three_squares = set([i + j for i in squares for j in two_squares])

if n == squares[-1]:
    print(1)
elif n in two_squares:
    print(2)
elif n in three_squares:
    print(3)
else:
    print(4)