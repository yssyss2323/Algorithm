n = int(input())
x = abs(n)
table = [0] * (x+1)
if x >= 1:
    table[1] = 1
for i in range(2,x+1):
    table[i] = (table[i-1] + table[i-2]) % 1000000000
if n > 0:
    print(1)
elif n == 0:
    print(0)
else:
    print(1 if n % 2 else -1)
print(table[-1])