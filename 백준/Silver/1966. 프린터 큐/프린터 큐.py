# ---- 5번 프린터 큐

import sys
from collections import deque

# sys.stdin = open("input.txt","rt")
data = sys.stdin.readline
test_case_num = int(data())
test_case = []
answers = []
def printer(N, M, list):
    imp_queue = deque()
    for i in range(N):
        imp_queue.append([i, list[i]])

    # print("imp_queue[M] : ", imp_queue[M])

    print_seq = {}
    count = 0

    while len(imp_queue):
        flag = imp_queue.popleft()
        if len(imp_queue) and flag[1] < max(imp_queue, key=lambda x:x[1])[1]: # 나보다 중요도 높은 문서가 있다면
            imp_queue.append(flag)
        else:
            count += 1
            print_seq[flag[0]] = count

    # M번째 문서가 몇 번째로 출력되는지 확인
    # print(f"M 번째 문서 (index {M}) 는 {print_seq[M]} 번째로 출력됩니다.")
    answers.append(print_seq[M])

for _ in range(test_case_num):
    test_case.append(list(map(int, data().strip().split())))
    test_case.append(list(map(int, data().strip().split())))

for n in range(test_case_num):
    printer(test_case[n*2][0], test_case[n*2][1], test_case[n*2+1])

# print("\n".join(answers))
print(*answers, sep="\n")