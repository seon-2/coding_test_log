from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    maps[0][0] = 0  # 방문한 곳을 0으로 표시

    while queue:
        x, y, dist = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny, dist + 1))

    return -1