# 딕셔너리 사용
# 들어왔다가 안 나간 사람이 회사에 있는 사람
# 들어온 상태 0, 나간 상태 : 1 -> 상태가 0인 것만 출력

from sys import stdin as s

N = int(s.readline().rstrip())

data = []
for i in range(N):
    data.append((s.readline().rstrip().split()))

log_dic = {}

for d in data:
    if d[1] == 'enter':
        log_dic[d[0]] = 0
    else:
        log_dic[d[0]] = 1

log_list = [k for k, v in log_dic.items() if v == 0]
sorted_list = sorted(log_list, reverse=True)
print("\n".join(sorted_list))