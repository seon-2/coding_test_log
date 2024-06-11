from collections import deque

N, K = map(int, input().strip().split())


def bfs(N, K):
    if N >= K:
        # N이 K보다 크거나 같다면 뒤로 걸어가기만 하면 됨
        return N - K

    # 최대 위치 크기
    max_pos = 100000
    # 방문 여부를 확인하는 배열
    visited = [False] * (max_pos + 1)
    # 큐 초기화
    queue = deque([(N, 0)])  # (현재 위치, 시간)
    visited[N] = True

    while queue:
        position, time = queue.popleft()

        # 현재 위치가 동생의 위치라면 시간을 반환
        if position == K:
            return time
        
        # 이동할 수 있는 모든 위치를 큐에 추가
        for next_pos in (position - 1, position + 1, position * 2):
            if 0 <= next_pos <= max_pos and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))


print(bfs(N, K))
