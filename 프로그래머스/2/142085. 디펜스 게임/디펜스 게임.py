import heapq

def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)
    
    heap = []
    total_enemy = 0
    
    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        total_enemy += e
        
        if total_enemy > n:
            if k > 0:
                k -= 1
                total_enemy += heapq.heappop(heap)
            else:
                return i
    
    return len(enemy)