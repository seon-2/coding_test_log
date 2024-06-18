n = int(input())

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 0×2 직사각형은 채우는 방법이 1가지
    if n > 0:
        dp[1] = 1  # 2×1 직사각형은 채우는 방법이 1가지
        for i in range(2, n + 1):
            dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

    return dp[n]

print(solution(n))