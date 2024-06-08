# 입력
T = int(input())
cases = [int(input()) for _ in range(T)]


def max_stepping_stones(N):
    left, right = 1, int((2 * N) ** 0.5) + 1  # k의 범위 설정
    while left < right:
        mid = (left + right + 1) // 2
        if mid * (mid + 1) // 2 <= N:
            left = mid
        else:
            right = mid - 1
    return left


for N in cases:
    print(max_stepping_stones(N))