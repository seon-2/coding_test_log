def count_cases(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 0을 만드는 방법은 1가지 (아무것도 선택하지 않음)

    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]  # 1을 선택하는 경우
        if i >= 2:
            dp[i] += dp[i - 2]  # 2를 선택하는 경우
        if i >= 3:
            dp[i] += dp[i - 3]  # 3을 선택하는 경우

    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_cases(n))