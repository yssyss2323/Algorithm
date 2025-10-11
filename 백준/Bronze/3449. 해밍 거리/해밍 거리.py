for _ in range(int(input())):
    num1 = int(input(), 2)
    num2 = int(input(), 2)
    cnt = bin(int(num1^num2))[2:].count('1')
    print(f"Hamming distance is {cnt}.")