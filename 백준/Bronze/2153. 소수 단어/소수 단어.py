word = input()

dictionary = {chr(i):i + 1 - ord('a') for i in range(ord('a'), ord('z') + 1)}
dictionary2 = {chr(i):i + 27 - ord('A') for i in range(ord('A'), ord('Z') + 1)}
dictionary.update(dictionary2)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = sum([dictionary[word[i]] for i in range(len(word))])
if is_prime(num):
    print("It is a prime word.")
else:
    print("It is not a prime word.")