import sys

# 입력 받기
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 동적 프로그래밍 적용
for i in range(1, n):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])  # 현재 집을 빨강으로 칠했을 때 최소 비용
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])  # 현재 집을 초록으로 칠했을 때 최소 비용
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])  # 현재 집을 파랑으로 칠했을 때 최소 비용

# 마지막 집의 최소 비용 출력
print(min(arr[n - 1]))