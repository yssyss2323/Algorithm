# 00.. 0부터 x99..9(9는 n개)까지의 숫자를 카운팅
def sub_counting(x, n, arr):
    key = n * 10 ** (n - 1)
    for i in range(10):
        arr[i] += key * (x + 1)
        if i <= x:
            arr[i] += 10 ** n

# 00.. 0부터 일반적인 수 m까지의 숫자를 카운팅
def general_counting(m):
    arr = [0 for _ in range(10)]
    if m < 0:
        return arr
    m = str(m)
    length = len(m)
    for i in range(length - 1):
        a = int(m[i]) - 1
        b = length - i - 1
        if a != -1:
            sub_counting(a, b, arr)
        arr[int(m[i])] += int(m[i + 1:]) + 1
    last_num = int(m[length - 1])
    for i in range(last_num + 1):
        arr[i] += 1
    return arr

# 각 숫자의 개수를 체크한 배열에서 합을 리턴
def sum_of_num(arr):
    ans = 0
    for i in range(1, 10):
        ans += arr[i] * i
    return ans

# 정답 구하기
L, U = map(int, input().split())
check1 = general_counting(U)
check2 = general_counting(L - 1)
answer = sum_of_num(check1) - sum_of_num(check2)
print(answer)
