def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

num = input()
if '.' not in num:
    print(f"{num}/1")
elif '(' not in num:
    integer, decimal = num.split('.')
    length_dec = len(decimal)
    integer = int(integer)
    decimal = int(decimal)

    dec_mom = 10 ** length_dec
    dec_daughter = dec_mom * integer + decimal
    dec_gcd = gcd(dec_mom, dec_daughter)
    dec_mom, dec_daughter = dec_mom // dec_gcd, dec_daughter // dec_gcd
    print(f"{dec_daughter}/{dec_mom}")
else:
    integer, decimal = num.split('.')
    idx = decimal.find('(')

    length_dec = len(decimal[idx + 1:-1])
    integer = int(integer) * 10 ** idx
    if idx:
        integer += int(decimal[:idx])
    decimal = int(decimal[idx + 1:-1])

    dec_mom = (10 ** length_dec - 1)
    dec_daughter = dec_mom * integer + decimal
    dec_mom *= 10 ** idx
    dec_gcd = gcd(dec_mom, dec_daughter)
    dec_mom, dec_daughter = dec_mom // dec_gcd, dec_daughter // dec_gcd
    print(f"{dec_daughter}/{dec_mom}")
