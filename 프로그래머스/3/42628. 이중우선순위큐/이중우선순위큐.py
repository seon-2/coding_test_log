import heapq

def solution(operations):
    min_heap = [] # 최소힙
    max_heap = [] # 최대힙
    
    for op in operations:
        command, data = map(str, op.split(" "))
        number = int(data)
        if command == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
        elif min_heap and max_heap and command == "D":
            if number == 1: # 최댓값 삭제
                max_value = heapq.heappop(max_heap)
                min_heap.remove(-max_value) # 최소힙 리스트에서도 해당 
            else: # 최소값 삭제
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)   
    
    if min_heap and max_heap: # 비어있지 않으면
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]