def solution(picks, minerals):
    answer = 0
    rounds = []
    
    for i in range(0, len(minerals), 5):
        minerals_to_mine = minerals[i:i+5]
        print(minerals_to_mine)
        diamond = iron = stone = 0
        
        for mineral in minerals_to_mine:
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
        rounds.append((diamond, iron, stone))
           
    print(rounds)
    for mine in sorted(rounds[0:sum(picks)], key=lambda x:x[2], reverse=True):
        if picks[0] > 0:
            answer += mine[0]
            picks[0] -= 1
        elif picks[1] > 0:
            answer += mine[1]
            picks[1] -= 1
        elif picks[2] > 0:
            answer += mine[2]
            picks[2] -= 1
        else:
            break
    return answer