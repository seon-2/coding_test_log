from collections import deque

answers = []
while True:
    number = int(input())
    if number == 0:
        break
    
    dq = deque(str(number))
    is_palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            is_palindrome = False
            break
    
    answers.append('yes' if is_palindrome else 'no')

print('\n'.join(answers))