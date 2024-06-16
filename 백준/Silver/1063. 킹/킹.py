from sys import stdin as s

chess = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
k, r, n = map(str, s.readline().strip().split())
# 왼쪽 아래 코너가 A1
king = [ord(k[0])-64, int(k[1])]
rock = [ord(r[0])-64, int(r[1])]
moves = [(s.readline().strip()) for _ in range(int(n))]

for move in moves:
    x, y = chess[move]
    if king[0] + x < 1 or king[0] + x > 8 or king[1] + y < 1 or king[1] + y > 8:
        continue
    else:
        king[0] += x
        king[1] += y

    if king == rock: # 킹과 돌이 겹치는 경우
        # 근데 돌이 못 움직이면 킹도 취소
        if rock[0] + x < 1 or rock[0] + x > 8 or rock[1] + y < 1 or rock[1] + y > 8:
            king[0] -= x
            king[1] -= y
            continue
        else: # 킹이 돌 쪽으로 움직인 방향으로 돌도 움직여야 함.
            rock[0] += x
            rock[1] += y

moving_king = chr(king[0]+64)+str(king[1])
moving_rock = chr(rock[0]+64)+str(rock[1])
print(moving_king, moving_rock)