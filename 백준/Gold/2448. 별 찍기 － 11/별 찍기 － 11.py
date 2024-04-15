top = ' ' * 2 + '*' + ' ' * 2
mid = ' ' + '*' + ' ' + '*' + ' '
bot = '*' * 5
triangle = [top, mid, bot]

start = 3
goal = int(input())
while goal > start:
    half_length = start
    start *= 2
    first, second = [], []
    for i in triangle:
        first.append(' ' * half_length + i + ' ' * half_length)
        second.append(i + ' ' + i)
    triangle = first + second
for i in triangle:
    print(i)
