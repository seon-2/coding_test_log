# 0 : 최소힙 출력, 그 값 제거 (배열이 비어 있으면 0 출력)
# 자연수 : 배열에 값 넣기

import sys
from heapq import *
# sys.stdin = open("input.txt", "rt")
data = sys.stdin.readline

N = int(data())
input_data = list(int(data().strip()) for _ in range(N))
heap = []
heapify(heap)
output = []

for number in input_data:
    if number == 0:
        if heap:
            output.append(heappop(heap))
        else:
            output.append(0)
    else:
        heappush(heap, number)

print("\n".join(map(str, output)))