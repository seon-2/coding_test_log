import sys
from collections import deque

input = sys.stdin.read
data = input().split()
index = 0

test_case_num = int(data[index])
index += 1
answers = []

def printer(N, M, priorities):
    imp_queue = deque((i, priorities[i]) for i in range(N))
    count = 0

    while imp_queue:
        flag = imp_queue.popleft()
        if any(flag[1] < item[1] for item in imp_queue):  # 나보다 중요도 높은 문서가 있다면
            imp_queue.append(flag)
        else:
            count += 1
            if flag[0] == M:
                return count

for _ in range(test_case_num):
    N = int(data[index])
    M = int(data[index + 1])
    index += 2
    priorities = list(map(int, data[index:index + N]))
    index += N
    answers.append(printer(N, M, priorities))

print(*answers, sep="\n")
