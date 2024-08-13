def solution(storey):
    answer = 0
    # new_storey = list(str(storey))
    new_storey = list(map(int, list((str(storey)))))
    
    print(new_storey)
    for i in range(len(new_storey)-1, -1, -1):
        number = new_storey[i]
        if number > 5:
            answer += 10 - number
            if i > 0:
                new_storey[i-1] += 1
            else:
                answer += 1
        elif number == 5:
            if new_storey[i-1] > 4 and i > 0:
                answer += 10 - number
                new_storey[i-1] += 1
            else:
                answer += number
        else:
            answer += number
        print(new_storey, answer)
    return answer

# 1 2 3 4 / 5 / 6 7 8 9