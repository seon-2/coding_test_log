from collections import deque

def bfs(l, start, end):
    if start == end:
        return 0
    
    directions = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    
    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if (nx, ny) == end:
                    return moves + 1
                queue.append((nx, ny, moves + 1))
                visited[nx][ny] = True
    
    return -1

def solve_knight_moves(test_cases):
    results = []
    for case in test_cases:
        l, start, end = case
        result = bfs(l, start, end)
        results.append(result)
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    test_cases = []
    for _ in range(t):
        l = int(data[idx])
        idx += 1
        start = (int(data[idx]), int(data[idx+1]))
        idx += 2
        end = (int(data[idx]), int(data[idx+1]))
        idx += 2
        test_cases.append((l, start, end))
    
    results = solve_knight_moves(test_cases)
    
    for result in results:
        print(result)
