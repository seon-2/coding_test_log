from sys import stdin as s

def longest_decreasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # 모든 위치에서 길이가 최소 1인 감소하는 부분 수열이 존재

    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

N = int(s.readline().strip())
A = list(map(int, s.readline().strip().split()))

print(longest_decreasing_subsequence(A))