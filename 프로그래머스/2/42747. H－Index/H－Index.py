def solution(citations):
    c_len = len(citations)
    answer = 0
    
    # 정렬
    c_sorted = sorted(citations)
    
    for i in range(c_len+1, 0, -1):
        if c_len >= i and c_sorted[c_len - i] >= i:
            answer = i
            break
    
    return answer

# [0, 1, 3, 5, 6]
# 5편의 논문 중 3번이상 인용된 논문이 3편 이상이고 나머지 논문이 3번 이하 인용되었다면 h-index가 3
# 일단 0을 다 빼야할까
# 최대값도 len이고 정답도 index?
