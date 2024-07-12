def find_sol(string,idx=0, ans_arr=[]):
    if string:
        min_char = min(string)
        min_idx = string.index(min_char)
        # step 1 : 현재 문자열에서 가장 빠른 문자를 찾아 그 인덱스를 저장
        ans_arr.append(idx + min_idx)
        # step 2 : 해당 문자 오른쪽 부분문자열에서 반복
        find_sol(string[min_idx+1:],idx + min_idx+1, ans_arr)
        # step 3 : 해당 문자 왼쪽 부분문자열에서 반복
        find_sol(string[:min_idx],idx, ans_arr)
    return ans_arr

string = input()
idx_list = []
for idx in find_sol(string):
    idx_list.append(idx)
    idx_list.sort()
    tmp = []
    for tmp_idx in idx_list:
        tmp += string[tmp_idx]
    print(''.join(tmp))