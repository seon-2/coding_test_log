# 시간복잡도 개선

def solution(citations):
    n = len(citations)
    max_val = max(citations)
    count = [0] * (max_val + 1)

    # 각 인용 횟수에 해당하는 논문 수 계산
    for c in citations:
        count[c] += 1

    total = 0
    
    for i in range(max_val, -1, -1):
        total += count[i]
        if total >= i:
            return i

    return 0