def bfs(idx):
    from collections import deque

    q = deque([idx])
    visited[idx] = True
    while q:
        idx = q.popleft()
        for i in graph[idx]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

# 그래프 초기 설정
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색 시작
visited = [False] * (n + 1)
bfs(1)

# 정답 구하기 - 1번을 제외한, 방문한 노드의 갯수가 정답!
answer = 0
for i in range(2, n + 1):
    if visited[i]:
        answer += 1
print(answer)
