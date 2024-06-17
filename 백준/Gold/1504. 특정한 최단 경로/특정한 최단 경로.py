import heapq
import sys

input = sys.stdin.read
INF = float('inf')

def dijkstra(graph, start):
    distance = [INF] * (len(graph))
    distance[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distance[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance_via_current = current_distance + weight
            if distance_via_current < distance[neighbor]:
                distance[neighbor] = distance_via_current
                heapq.heappush(priority_queue, (distance_via_current, neighbor))
    
    return distance

def main():
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    E = int(data[idx])
    idx += 1
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(E):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    v1 = int(data[idx])
    idx += 1
    v2 = int(data[idx])
    
    distance_from_1 = dijkstra(graph, 1)
    distance_from_v1 = dijkstra(graph, v1)
    distance_from_v2 = dijkstra(graph, v2)
    
    path1 = distance_from_1[v1] + distance_from_v1[v2] + distance_from_v2[N]
    path2 = distance_from_1[v2] + distance_from_v2[v1] + distance_from_v1[N]
    
    result = min(path1, path2)
    
    if result >= INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
