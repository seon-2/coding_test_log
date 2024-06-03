# 9×9에서 최댓값과 해당 위치 찾기

import sys
input = sys.stdin.read

data = input().strip().split()
grid = []

# 입력값을 9×9로 변환
for i in range(9):
    row = list(map(int, data[i*9:(i+1)*9]))
    grid.append(row)

max_value = -1
max_row = -1
max_col = -1

for i in range(9):
    for j in range(9):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            max_row = i
            max_col = j

print(max_value)
print(max_row + 1, max_col + 1)
