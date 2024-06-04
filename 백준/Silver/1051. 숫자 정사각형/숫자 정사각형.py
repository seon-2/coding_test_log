import sys
# sys.stdin = open("input.txt","rt")

read = sys.stdin.readline

N, M = map(int, read().split())
rect = [list(map(int, input())) for _ in range(N)]

def is_square(size):
    for i in range(N - size + 1):
        for j in range(M - size + 1):
            # 네 꼭짓점의 숫자가 같은지 확인
            if rect[i][j] == rect[i][j + size - 1] == rect[i + size - 1][j] == rect[i + size - 1][j + size - 1]:
                return True
    return False

# 모든 가능한 정사각형 크기 검사
for size in range(min(N, M), 0, -1):
    if is_square(size):
        print(size**2)
        break
