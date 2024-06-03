# 가로로 끝까지 순회, 세로로도

import sys
# sys.stdin=open("input.txt","rt")
data = sys.stdin.readline

# 입력 받기
N = int(input().strip())
room = [input().strip() for _ in range(N)]

# 가로로 누울 수 있는 자리 수 세기
horizontal_count = 0
for row in room:
    count = 0
    for char in row:
        if char == '.':
            count += 1
        else:
            if count >= 2:
                horizontal_count += 1
            count = 0
    if count >= 2:
        horizontal_count += 1

# 세로로 누울 수 있는 자리 수 세기
vertical_count = 0
for col in range(N):
    count = 0
    for row in range(N):
        if room[row][col] == '.':
            count += 1
        else:
            if count >= 2:
                vertical_count += 1
            count = 0
    if count >= 2:
        vertical_count += 1

print(horizontal_count, vertical_count)
