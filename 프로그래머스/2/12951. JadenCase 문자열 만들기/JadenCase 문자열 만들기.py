def solution(s):

    list = s.split(' ')
    answer = []

    for v in list:
        answer.append(v.capitalize())

    return " ".join(answer)