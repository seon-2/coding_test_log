from heapq import *

def solution(scoville, K):
    
    if sum(scoville) == 0 and K > 0: # 모든 값이 0이라면 [0, 0, ...] 
        count = -1 # 모든 음식의 스코빌을 K이상으로 만들 수 없음
    else:
        count = 0
        heapify(scoville) # scoville 리스트를 힙으로 변경
        
        while scoville[0] < K:# 가장 작은 값이 K보다 작다면 더 섞어야 함
            if len(scoville) < 2:
                count = -1
                break
            
            mixed_food = heappop(scoville) + heappop(scoville) * 2 # 섞고
            count += 1
            heappush(scoville, mixed_food) # 가진 음식에 추가

    return count

