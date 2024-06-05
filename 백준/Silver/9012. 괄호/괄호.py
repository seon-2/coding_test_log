# ---- 7번 괄호
# 스택 사용
# 올바른 괄호이면 y, 아니면 n 올바른 괄호란, (열고 닫히고 조합) 맞는 것
# 열리는 괄호이면 스택에 넣고 닫히는 괄호 이면 마지막 열리는 괄호 pop
# 닫히는 괄호가 먼저 들어오면 n
# 끝까지 다 돌고 스택에 남아있으면 n

import sys
# sys.stdin = open("input.txt","rt")
data = sys.stdin.readline

T = int(data())
test_data = [data().strip() for _ in range(T)]

def is_vps(string):
    if string[0] == ')':
        return False

    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if stack: # 스택에 값이 남아있으면
        return False
    else:
        return True

for str in test_data:
    print("YES" if is_vps(str) else "NO")
