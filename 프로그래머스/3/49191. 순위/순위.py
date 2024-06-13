from collections import defaultdict, deque

def solution(n, results):
    # 이긴 관계와 진 관계를 저장할 그래프
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)
    
    # 주어진 결과를 그래프에 기록
    for winner, loser in results:
        win_graph[winner].add(loser)
        lose_graph[loser].add(winner)
    
    # BFS를 통한 승리/패배 관계 확장
    def bfs(start, graph):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited
    
    # 모든 선수에 대해 이긴 관계와 진 관계를 확장
    win = defaultdict(set)
    lose = defaultdict(set)
    for player in range(1, n + 1):
        win[player] = bfs(player, win_graph)
        lose[player] = bfs(player, lose_graph)
    
    # 정확한 순위를 매길 수 있는 선수 수를 계산
    answer = 0
    for player in range(1, n + 1):
        if len(win[player]) + len(lose[player]) == n - 1:
            answer += 1
    
    return answer

# 정확하게 순서 매기는??
# 5 : 확인 X, 2에게 짐 => 2에게 졌다는 건, 1,3,4에게도 진다는 말. win = 0, lose = 3 + 1
# 4 : 3, 2 이김, 진거 확인 X win = 2, lose = 0
# 3 : 2 이김, 4에게 짐 => win = 1, lose = 1
# 2 : 5 이김, 1,3,4에게 짐 => 순위 확인 가능 => win = 1, lose = 3
# 1 : 2 이김, 진거 확인 X => win = 1, lose = 0