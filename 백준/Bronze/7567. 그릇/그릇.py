# ---- 4번 그릇
# 왼쪽부터 하나씩 빼면서 처음에는 +10, 같으면 +5, 다르면 +10
# 왼쪽부터 해야하니 queue 사용

import sys
from collections import deque
# sys.stdin = open("input.txt","rt")

data = list(sys.stdin.readline().strip())
plates = deque()
for plate in data:
    plates.append(plate)

height = 10
flag = plates.popleft()

while len(plates):
    now = plates.popleft()
    if flag == now:
        height += 5
    else:
        height += 10
    flag = now

print(height)