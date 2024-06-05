import sys
from collections import deque

# sys.stdin = open("input.txt", "rt")
data = sys.stdin.readline

# 입력 처리
N, M = map(int, data().split())
targets = list(map(int, data().split()))

# 양방향 순환 큐 만들기
queue = deque(range(1, N + 1))
operations = 0

for target in targets:
    while True:
        if target == queue[0]:
            queue.popleft()
            break
        
        target_index = queue.index(target)
        if target_index < len(queue) / 2:  # 앞쪽이 가까움
            queue.append(queue.popleft())  # 왼쪽으로 한 칸 이동
        else:
            queue.appendleft(queue.pop())  # 오른쪽으로 한 칸 이동
        operations += 1

print(operations)
