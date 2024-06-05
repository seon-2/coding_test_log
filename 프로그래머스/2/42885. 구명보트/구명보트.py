from collections import deque

def solution(people, limit):
    answer = 0
    sorted_by_weigh = sorted(people)
    queue = deque()
    
    for person in sorted_by_weigh:
        queue.append(person)
        
    lighter = 0
    heavier = 0
        
    while queue:
        
        if lighter == 0 and queue:
            lighter = queue.popleft() 
        
        if heavier == 0 and queue:
            heavier = queue.pop() 
        
        # 태울 수 있음. 둘 보내기 
        if lighter + heavier <= limit:
            answer += 1
            lighter = 0
            heavier = 0
        else: # 태울 수 없음
            answer += 1
            heavier = 0
              
    
    if lighter != 0: 
        answer += 1
    
    return answer
