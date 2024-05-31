# 들어오는 문자 확인, set()에 넣어서 중복 제거
# ENTER이거나 마지막에는 set 길이를 정답에 더하고 set 초기화

from sys import stdin as s

N = int(s.readline().rstrip())

answer = 0
data_set = set()
for i in range(N+1):
    str = (s.readline().rstrip())
    if str == 'ENTER' or i == N:
        answer += len(data_set)
        data_set = set()
    else:
        data_set.add(str)

print(answer)