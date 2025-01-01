str1 = 'aiyeou'
str2 = str1.upper()
str3 = 'bkxznhdcwgpvjqtsrlmf'
str4 = str3.upper()

def func(sentence):
    ans = ''
    for ch in sentence:
        if ch in str1:
            i = str1.find(ch)
            j = (i + 3) % len(str1)
            ans += str1[j]
        elif ch in str2:
            i = str2.find(ch)
            j = (i + 3) % len(str2)
            ans += str2[j]
        elif ch in str3:
            i = str3.find(ch)
            j = (i + 10) % len(str3)
            ans += str3[j]
        elif ch in str4:
            i = str4.find(ch)
            j = (i + 10) % len(str4)
            ans += str4[j]
        else:
            ans += ch
    print(ans)


while True:
    try:
        sentence = input()
        func(sentence)
    except:
        break