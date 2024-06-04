def solution(name):
    answer = 0
    # 커서 위, 아래 이동 : 아스키코드로, N이 13번, O부터는 거꾸로가 더 빠름. 12번
    # 커서 왼, 오 이동 : 정방향 OR 역방향 이동. 
    
    min_move = len(name) - 1  # 처음에는 끝까지 이동할 수 있다고 가정
    
    for i, char in enumerate(name):        
            
        if ord(char) > 78: # O 이후 알파벳
            answer += 91 - ord(char)
        else:
            answer += ord(char) - 65
        
        # 연속된 'A' 구간의 길이
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        # 왼쪽 또는 오른쪽 움직임 계산
        min_move = min(min_move, i + len(name) - next_idx + min(i, len(name) - next_idx))
    
    
    return answer + min_move