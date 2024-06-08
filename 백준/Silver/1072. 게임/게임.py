import sys
input = sys.stdin.read
data = input().strip().split()
cases = [(int(data[i]), int(data[i+1])) for i in range(0, len(data), 2)]


def min_games_to_increase_win_rate(X, Y):
    current_rate = (Y * 100) // X
    
    # 승률이 절대 변하지 않는 경우
    if current_rate >= 99:
        return -1
    
    left, right = 0, 2 * 10**9  # 충분히 큰 값으로 초기화
    
    while left < right:
        mid = (left + right) // 2
        new_rate = ((Y + mid) * 100) // (X + mid)
        
        if new_rate > current_rate:
            right = mid
        else:
            left = mid + 1
            
    return left


for X, Y in cases:
    print(min_games_to_increase_win_rate(X, Y))
