transform = {' *** * * * * * * ***': 0,
             '   *   *   *   *   *': 1,
             ' ***   * *** *   ***': 2,
             ' ***   * ***   * ***': 3,
             ' * * * * ***   *   *': 4,
             ' *** *   ***   * ***': 5,
             ' *** *   *** * * ***': 6,
             ' ***   *   *   *   *': 7,
             ' *** * * *** * * ***': 8,
             ' *** * * ***   * ***': 9}

save = []
for _ in range(5):
    tmp = ' ' + input()
    for i in range(len(tmp) // 4):
        save.append(tmp[4 * i: 4 * i + 4])

cnt = len(save) // 5
numbers = [''] * cnt
for i in range(5):
    for j in range(cnt):
        numbers[j] += save[i * cnt + j]

try:
    real_nums = [transform[num] for num in numbers]
    if real_nums[-1] % 2 == 0 and sum(real_nums) % 3 == 0:
        print('BEER!!')
    else:
        print("BOOM!!")
except:
    print('BOOM!!')
