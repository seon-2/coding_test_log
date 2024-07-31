import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    element_set = set()  # 현재 큐에 있는 요소를 추적하는 집합
    
    for op in operations:
        command, data = op.split()
        if command == "I":
            num = int(data)
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            element_set.add(num)
        elif element_set and command == "D":
            if data == "1":  # 최댓값 삭제
                while max_heap and -max_heap[0] not in element_set:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_value = -heapq.heappop(max_heap)
                    element_set.remove(max_value)
            else:  # 최솟값 삭제
                while min_heap and min_heap[0] not in element_set:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_value = heapq.heappop(min_heap)
                    element_set.remove(min_value)
    
    # 최종 정리
    while max_heap and -max_heap[0] not in element_set:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0] not in element_set:
        heapq.heappop(min_heap)
    
    if element_set:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]