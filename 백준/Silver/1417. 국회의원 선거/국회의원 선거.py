# 입력
n = int(input())
votes = [int(input()) for _ in range(n)]


def min_bribes_to_win(n, votes):
    # 다솜이의 현재 득표수
    dasom_votes = votes[0]
    # 다른 후보들의 득표수 리스트
    other_votes = votes[1:]
    
    # 매수한 사람의 수
    bribes = 0
    
    # 다솜이가 최대 득표자가 될 때까지 반복
    while other_votes and dasom_votes <= max(other_votes):
        # 가장 득표수가 많은 후보의 표를 하나 매수
        max_votes = max(other_votes)
        max_index = other_votes.index(max_votes)
        
        # 매수하여 다솜이에게 추가
        other_votes[max_index] -= 1
        dasom_votes += 1
        bribes += 1
    
    return bribes


# 결과 출력
print(min_bribes_to_win(n, votes))
