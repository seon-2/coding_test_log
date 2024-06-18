def solution(N):
    # dp 배열 초기화, 모든 값을 False로 설정
    dp = [False] * (N + 1)
    
    # Base cases
    dp[1] = True  # 돌이 1개일 때, 상근이가 이김
    
    if N >= 3:
        dp[3] = True  # 돌이 3개일 때, 상근이가 이김
    
    for i in range(4, N + 1):
        # 돌을 1개 또는 3개 가져갈 수 있음
        # 상대방이 패배하는 경우에 내가 이길 수 있음
        dp[i] = not dp[i - 1] or not dp[i - 3]
    
    return "SK" if dp[N] else "CY"

# 입력 받기
N = int(input())

# 결과 출력
print(solution(N))
