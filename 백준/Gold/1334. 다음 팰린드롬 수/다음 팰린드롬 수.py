def list_to_num(arr):
    tmp = ''
    for i in arr:
        tmp += str(i)
    return int(tmp)

nlist = list(map(int,input()))
input_num = list_to_num(nlist)
length = len(nlist)
mid = (length + 1) // 2

base_list = [0] * length
for i in range(mid):
    base_list[i] = base_list[length-1-i] = nlist[i]
base_num = list_to_num(base_list)

if base_num > input_num:
    print(base_num)
else:
    for i in reversed(range(mid)):
        if base_list[i] < 9:
            base_list[i] += 1
            base_list[length-i-1] = base_list[i]
            for j in range(i+1,length-i-1):
                base_list[j] = 0
            print(list_to_num(base_list))
            break
        else:
            continue
    else:
        answer = '1' + '0' * (length - 1) + '1'
        print(answer)