from sys import stdin as s
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  # 방문 처리
    count = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                count += 1

    return count


n = int(s.readline())
graph = [list(map(int, s.readline().rstrip())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)