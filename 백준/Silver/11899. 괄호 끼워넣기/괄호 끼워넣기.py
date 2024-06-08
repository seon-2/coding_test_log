# 올바른 괄호는 pop, stack에 남아있는 개수 출력

S = input().strip()


def get_num_of_remaining(string):
    stack = []
    for char in string:
        if char == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(char)
    return len(stack)


print(get_num_of_remaining(S))