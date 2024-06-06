# 음수 힙, 양수 힙 따로 만들기

import sys
import heapq

data = sys.stdin.readline
N = int(data())
operations = [int(data()) for _ in range(N)]

def abs_heap(operations):
    neg_heap = []  # 음수 힙
    pos_heap = []  # 양수 힙
    output = []

    for op in operations:
        if op != 0:
            value = abs(op)
            if op < 0:
                heapq.heappush(neg_heap, (value, op))
                heapq.heappush(pos_heap, (-value, -op))
            else:
                heapq.heappush(neg_heap, (value, op))
                heapq.heappush(pos_heap, (-value, op))
        else:
            if not neg_heap:
                output.append(0)
            else:
                value = heapq.heappop(neg_heap)[1]
                output.append(value)
                heapq.heappop(pos_heap)

    return output

result = abs_heap(operations)
print('\n'.join(map(str, result)))