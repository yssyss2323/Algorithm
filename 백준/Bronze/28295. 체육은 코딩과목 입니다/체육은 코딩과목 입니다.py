direct = ['N', 'E', 'S', 'W']
curr = 0
for _ in range(10):
    curr = (curr + int(input())) % 4
print(direct[curr])