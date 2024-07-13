string = input()
bomb = input()
length = len(bomb)

idx = 0
stack = []
ans = []
for ch in string:
    # 폭탄 첫번째 문자 -> 언제나 스택에 넣어준다
    if ch == bomb[0]:
        stack.append(ch)
        idx = 1
        if length == 1:
            stack.pop()
            idx = 0
        continue
    # 스택에 뭔가 들어있는 경우
    if stack:
        # case 1 : 지금 들어올 문자 ch가 폭탄 순서에 알맞는 경우
        if ch == bomb[idx]:
            stack.append(bomb[idx])
            idx += 1
            if idx == length:
                for _ in range(length):
                    stack.pop()
                idx = bomb.index(stack[-1]) + 1 if stack else 0
        # case 2 : 폭턴 순서에 알맞지 않는 경우 -> 스택에 들어온 문자들은 싹다 못쓰게 됨
        else:
            ans += stack
            stack = []
            idx = 0
            ans.append(ch)
    # 폭탄의 첫문자가 아니면서 스택이 비어있는 경우 -> 폭탄을 만들 수 없는 문자임 -> ans에 넣어준다
    else:
        ans.append(ch)
ans += stack
print(''.join(ans) if ans else 'FRULA')