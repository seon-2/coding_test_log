from collections import defaultdict, deque

def bfs(graph, start, target):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        current, depth = queue.popleft()

        if current == target:
            return depth

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

    return -1

def solution(n, person1, person2, relations):
    graph = defaultdict(list)

    for parent, child in relations:
        graph[parent].append(child)
        graph[child].append(parent)

    return bfs(graph, person1, person2)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    person1 = int(data[1])
    person2 = int(data[2])
    m = int(data[3])
    relations = []

    index = 4
    for _ in range(m):
        parent = int(data[index])
        child = int(data[index + 1])
        relations.append((parent, child))
        index += 2

    print(solution(n, person1, person2, relations))
