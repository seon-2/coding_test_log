import heapq

def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    mix_count = 0
    
    while heap:
        min_val = heapq.heappop(heap)
        if min_val >= K:
            break
        if not heap:
            return -1
        
        second_min = heapq.heappop(heap)
        new_val = min_val + second_min * 2
        heapq.heappush(heap, new_val)
        mix_count += 1
        
    return mix_count