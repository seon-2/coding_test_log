# 별 찍기
# N이 5이면
# (*개수, ' '개수)일 떄
# (1,4) ... (5,0) 까지 갔다가 다시 (4,1) (3,2) 해서 (1,4)까지
# (5,0)은 1줄!!

from sys import stdin as s

N = int(s.readline())

for i in range(1, N+1):
    print('*' * i + ' ' * (N-i) + ' ' * (N-i) + '*' * i )

for i in range(N-1, 0, -1):
    print('*' * i + ' ' * (N-i) + ' ' * (N-i) + '*' * i )
