# 듣도 못한 사람과 보도 못한 사람의 교집합 찾기

from sys import stdin as s

N, M = map(int, s.readline().split())
hear_set = set()  # 듣도 못한 사람 집합
see_set = set()  # 보도 못한 사람 집합

for i in range(N):
    hear_set.add(s.readline().rstrip())

for j in range(M):
    see_set.add(s.readline().rstrip())

result = sorted(hear_set & see_set)

print(len(result))
print("\n".join(result))
