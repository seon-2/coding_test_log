# 확장자를 키로 딕셔너리 만들기
# 정렬해서 출력

from sys import stdin as s

N = int(s.readline().rstrip())

data = []
data_dic = {}

for i in range(N):
    data.append((s.readline().rstrip().split('.')))

for d in data:
    data_dic[d[1]] = data_dic.get(d[1], 0) + 1

for k, v in sorted(data_dic.items()):
    print(k, v)
