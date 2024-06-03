import sys

# 입력 받기
input_data = sys.stdin.read().strip().split('\n')

size = input_data[0].split()
row, col = map(int, size)
arr = [list(i) for i in input_data[1:]]

counts = []

white = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

black = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

def white_first(x, y):
    count = 0
    for i in range(8):
        for j in range(8):
            if arr[i + x][j + y] != white[i][j]:
                count += 1
    return count

def black_first(x, y):
    count = 0
    for i in range(8):
        for j in range(8):
            if arr[i + x][j + y] != black[i][j]:
                count += 1
    return count

# 전체 판을 움직이는 형태로 작성했기에, -7을 해줌으로써 전체 판을 벗어나지 않게 해준다.
for j in range(row - 7):
    for k in range(col - 7):
        counts.append(white_first(j, k))
        counts.append(black_first(j, k))

print(min(counts))
