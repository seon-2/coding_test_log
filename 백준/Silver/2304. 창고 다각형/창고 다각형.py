def calculate_min_area(pillars):
    # 기둥을 x 좌표 순으로 정렬
    pillars.sort()

    # 가장 높은 기둥 찾기
    highest_idx = 0
    highest = pillars[0][1]
    for i, (_, height) in enumerate(pillars):
        if height > highest:
            highest = height
            highest_idx = i

    # 왼쪽에서 오른쪽으로 탐색하여 면적 계산
    total_area = 0
    left_x, left_y = pillars[0]
    for i in range(highest_idx + 1):
        if pillars[i][1] >= left_y:
            height = left_y
            width = pillars[i][0] - left_x
            total_area += width * height
            left_x, left_y = pillars[i]
    
    # 오른쪽에서 왼쪽으로 탐색하여 면적 계산
    right_x, right_y = pillars[-1]
    for i in range(len(pillars) - 1, highest_idx - 1, -1):
        if pillars[i][1] >= right_y:
            height = right_y
            width = right_x - pillars[i][0]
            total_area += width * height
            right_x, right_y = pillars[i]

    # 가장 높은 기둥의 면적 추가
    total_area += highest

    return total_area


# 입력
N = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(N)]

print(calculate_min_area(pillars))
