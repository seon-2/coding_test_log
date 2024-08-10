from collections import deque

def solution(number, k):
    stack = deque()
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k > 0:
        stack = list(stack)[:-k]
    
    return ''.join(stack)