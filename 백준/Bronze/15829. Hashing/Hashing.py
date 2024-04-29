def hashing(given_string):
    H = 0
    for i in range(len(given_string)):
        tmp = ord(given_string[i]) - ord('a') + 1
        H += tmp * 31 ** i
    return H % 1234567891


L = int(input())
my_string = input()
print(hashing(my_string))
