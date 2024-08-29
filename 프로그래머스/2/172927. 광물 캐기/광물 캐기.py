def solution(picks, minerals):
    # 사용 가능한 곡괭이의 총 개수
    total_picks = sum(picks)
    
    # 광물을 5개씩 그룹화하되, 사용 가능한 곡괭이 수만큼만 고려
    mineral_groups = [minerals[i:i+5] for i in range(0, min(len(minerals), total_picks*5), 5)]
    
    # 각 그룹에 대한 피로도 계산
    fatigue_list = []
    for group in mineral_groups:
        diamond = iron = stone = 0
        for mineral in group:
            if mineral == 'diamond':
                diamond += 1
                iron += 5
                stone += 25
            elif mineral == 'iron':
                diamond += 1
                iron += 1
                stone += 5
            else:  # stone
                diamond += 1
                iron += 1
                stone += 1
        fatigue_list.append((diamond, iron, stone))
    
    # 돌 곡괭이로 캤을 때의 피로도를 기준으로 내림차순 정렬
    fatigue_list.sort(key=lambda x: x[2], reverse=True)
    
    # 피로도 계산
    total_fatigue = 0
    for fatigue in fatigue_list:
        if picks[0] > 0:  # 다이아몬드 곡괭이
            total_fatigue += fatigue[0]
            picks[0] -= 1
        elif picks[1] > 0:  # 철 곡괭이
            total_fatigue += fatigue[1]
            picks[1] -= 1
        elif picks[2] > 0:  # 돌 곡괭이
            total_fatigue += fatigue[2]
            picks[2] -= 1
        else:
            break  # 사용 가능한 곡괭이가 없으면 종료
    
    return total_fatigue