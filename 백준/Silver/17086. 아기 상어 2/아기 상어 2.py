from sys import stdin as s
from collections import deque

N, M = map(int, s.readline().strip().split())
matrix = [list(map(int, s.readline().split())) for _ in range(N)]

# BFS를 위한 큐 초기화
queue = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i, j))

# 상하좌우 및 대각선 이동을 위한 방향 벡터
moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# 거리 계산용 2차원 리스트 초기화
distances = [[-1] * M for _ in range(N)]
for x, y in queue:
    distances[x][y] = 0

# BFS 수행
while queue:
    x, y = queue.popleft()
    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < N and 0 <= ny < M and distances[nx][ny] == -1:
            distances[nx][ny] = distances[x][y] + 1
            queue.append((nx, ny))

# 최대 거리 계산
max_distance = 0
for i in range(N):
    for j in range(M):
        if distances[i][j] > max_distance:
            max_distance = distances[i][j]

print(max_distance)
