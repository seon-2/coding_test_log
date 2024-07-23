def solution(x, n):
    answer = []
    end = n*x+1
    if x == 0:
        return [0] * n
    elif x < 0:
        end = n*x-1
        
    for i in range(x, end, x):
        answer.append(i)
    return answer