from collections import deque

def solution(people, limit):
    answer = 0
    dq = deque(sorted(people)) # 오름차순 정렬
    # 제일 무거운 사람 먼저 태우고 가능하다면 가장 가벼운 사람 태우기
    
    while dq:
        if len(dq) > 1 and dq[-1] + dq[0] <= limit:
            dq.popleft()
        dq.pop()
        answer += 1
    
    return answer