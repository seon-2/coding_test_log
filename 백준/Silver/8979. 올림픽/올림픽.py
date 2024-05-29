# 국가의 수는 1000개 이하.
# 규칙에 따라 등수 구하기
# 공동 2등 다음은 4등

from sys import stdin as s

N, K = map(int, s.readline().split())

data = [list(map(int, s.readline().split())) for _ in range(N)]

data.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank = 0
prev_medals = (-1, -1, -1)
prev_rank = 1

for i in range(N):
    cur_medals = (data[i][1], data[i][2], data[i][3])

    if cur_medals != prev_medals:
        if i > 0 and data[i - 1][1:4] == prev_medals:
            rank = prev_rank
        else:
            rank = i+1
        prev_rank = rank
    data[i].append(rank)
    prev_medals = cur_medals

for i in range(N):
    if data[i][0] == K:
        print(data[i][4])
        break
