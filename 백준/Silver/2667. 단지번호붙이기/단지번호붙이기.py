from sys import stdin as s
from collections import deque


N = int(s.readline())
maps = [list(s.readline().strip()) for _ in range(N)]
houses = []
dq = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    dq.append([x, y])
    maps[x][y] = '2' # 방문처리
    count = 1

    while dq:
        now_x, now_y = dq.popleft()
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N: # 범위 안에 있다면
                if maps[new_x][new_y] == '1':
                    dq.append([new_x, new_y])
                    maps[new_x][new_y] = '2'
                    count += 1

    houses.append(count)

for i in range(N):
    for j in range(N):
        if maps[i][j] == '1':
            bfs(i, j)

print(len(houses))
for house in sorted(houses):
    print(house)
