from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0, 0)])
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for _ in range(m)]
    
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    return -1 if maps[m-1][n-1] == 1 else maps[m-1][n-1]