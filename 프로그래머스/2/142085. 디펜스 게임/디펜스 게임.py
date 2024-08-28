import heapq

def solution(n, k, enemy):
    answer = 0
    
    if len(enemy) <= k:
        return len(enemy)

    defense_heap = []

    for e in enemy:
        if e <= n:  # 일단 갈 수 있는데까지 가고
            n -= e
            answer += 1
            heapq.heappush(defense_heap, -e)
        elif k > 0:  # 막혔다면
            if defense_heap and -defense_heap[0] > e:  # 지나온 적 중 가장 큰 적이 현재 적보다 크다면
                n -= heapq.heappop(defense_heap) # 지나온 적의 수 만큼 다시 +
                n -= e # 현재 적 상대
                heapq.heappush(defense_heap, -e)
                answer += 1
            else:
                answer += 1 # 현재 적을 무적권으로 상대
            k -= 1

        else:
            break

    return answer
