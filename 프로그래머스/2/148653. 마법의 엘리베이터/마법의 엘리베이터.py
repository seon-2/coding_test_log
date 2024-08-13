def solution(storey):
    answer = 0
    digits = list(map(int, str(storey)))
    
    for i in reversed(range(len(digits))):
        current_digit = digits[i]
        
        if current_digit > 5 or (current_digit == 5 and i > 0 and digits[i-1] >= 5):
            answer += 10 - current_digit
            if i > 0:
                digits[i-1] += 1
            else:
                answer += 1
        else:
            answer += current_digit

    return answer
# 1 2 3 4 / 5 / 6 7 8 9
