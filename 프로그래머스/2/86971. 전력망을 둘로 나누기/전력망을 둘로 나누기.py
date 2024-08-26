def dfs(node, parent, graph):
    count = 1  # 현재 노드를 카운트
    for neighbor in graph[node]:
        if neighbor != parent:
            count += dfs(neighbor, node, graph)
    return count

def solution(n, wires):
    def make_graph():
        graph = [[] for _ in range(n+1)]
        for v1, v2 in wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph

    min_diff = float('inf')
    graph = make_graph()

    for v1, v2 in wires:
        # v1과 v2 사이의 전선을 끊음
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # 두 부분의 송전탑 개수 차이 계산
        count1 = dfs(v1, 0, graph)
        count2 = n - count1
        diff = abs(count1 - count2)

        # 최소 차이 갱신
        min_diff = min(min_diff, diff)

        # 끊은 전선 다시 연결
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_diff