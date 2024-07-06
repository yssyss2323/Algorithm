inputs = []
for _ in range(5):
    tmp = input()
    tmp += (15 - len(tmp)) * ' '
    inputs.append(tmp)

for i in range(15):
    for j in range(5):
        if inputs[j][i] != ' ':
            print(inputs[j][i],end='')