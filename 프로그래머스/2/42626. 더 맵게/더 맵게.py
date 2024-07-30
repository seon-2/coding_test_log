from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    mix_count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first + second * 2)
        mix_count += 1
    
    return mix_count