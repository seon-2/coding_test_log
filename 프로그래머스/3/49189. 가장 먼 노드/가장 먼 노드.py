from collections import deque, defaultdict

def solution(n, vertex):
    # 그래프 초기화 (인접 리스트)
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS를 위한 큐와 거리 기록용 리스트
    queue = deque([1])
    distances = [-1] * (n + 1)
    distances[1] = 0  # 시작 노드의 거리는 0
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드라면
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    # 가장 먼 거리와 그 거리를 가지는 노드의 개수 찾기
    max_distance = max(distances)
    return distances.count(max_distance)