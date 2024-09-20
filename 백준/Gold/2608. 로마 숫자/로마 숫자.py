def trans(string):
    dic1 = {'IV': 'P', 'IX': 'Q', 'XL': 'R', 'XC': 'S', 'CD': 'T', 'CM': 'U'}
    dic2 = {'I': 1, 'P': 4, 'V': 5, 'Q': 9, 'X': 10, 'R': 40, 'L': 50, 'S': 90, 'C': 100, 'T': 400, 'D': 500, 'U': 900,
            'M': 1000}

    for ch in dic1.keys():
        if ch in string:
            string = string.replace(ch, dic1[ch])
            continue

    num = 0
    for ch in string:
        num += dic2[ch]

    return num


def rev_trans(num):
    dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
           4: 'IV', 1: 'I'}

    string = ''
    for n in dic.keys():
        x, num = divmod(num, n)
        string += dic[n] * x

    return string


num1 = input()
num2 = input()

ans = trans(num1) + trans(num2)
print(ans)
print(rev_trans(ans))