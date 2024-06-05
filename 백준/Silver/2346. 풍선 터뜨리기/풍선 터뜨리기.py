import sys
from collections import deque
data = sys.stdin.readline

N = int(data())
queue = deque(enumerate(map(int, data().split())))
answer = []

while queue:
    idx, paper = queue.popleft()
    answer.append(idx + 1)

    if paper > 0:
        queue.rotate(-(paper - 1))
    elif paper < 0:
        queue.rotate(-paper)

print(' '.join(map(str, answer)))