def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순 정렬

    left, right = 0, len(people) - 1  # 투 포인터 초기화

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 태움
        right -= 1  # 무거운 사람 태움
        answer += 1

    return answer