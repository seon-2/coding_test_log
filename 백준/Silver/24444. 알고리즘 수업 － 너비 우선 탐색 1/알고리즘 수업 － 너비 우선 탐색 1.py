from collections import defaultdict, deque

def bfs(graph, start, visited, order):
    queue = deque([start])
    visited[start] = True
    order[start] = 1
    count = 1

    while queue:
        current = queue.popleft()

        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                order[neighbor] = count
                queue.append(neighbor)

def solution(n, m, r, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    order = [0] * (n + 1)

    bfs(graph, r, visited, order)

    for i in range(1, n + 1):
        print(order[i])

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    r = int(data[2])
    edges = []

    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    solution(n, m, r, edges)
