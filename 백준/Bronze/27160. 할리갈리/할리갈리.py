# 전체 다 돌면서 과일 개수 확인
# 딕셔너리 활용

from sys import stdin as s

N = int(s.readline())
data = [s.readline().strip().split() for _ in range(N)]
hali = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

for d in data:
    hali[d[0]] += int(d[1])

if 5 in list(hali.values()):
    print("YES")
else:
    print("NO")