n = int(input())
dancing = set()
dancing.add('ChongChong')
for _ in range(n):
    a, b = input().split()
    if a in dancing:
        if b not in dancing:
            dancing.add(b)
    else:
        if b in dancing:
            dancing.add(a)
print(len(dancing))
