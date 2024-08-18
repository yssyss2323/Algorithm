def check(word):
    l, r = 0, len(word) - 1
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            tmp1 = word[:l] + word[l+1:]
            tmp2 = word[:r] + word[r+1:]
            if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                return 1
            return 2
    return 0


t = int(input())
for _ in range(t):
    s = input()
    print(check(s))