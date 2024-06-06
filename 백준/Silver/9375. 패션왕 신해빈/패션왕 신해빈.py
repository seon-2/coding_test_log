# 의상 종류로 만들 수 있는 경우의 수

import sys
import collections
data = sys.stdin.readline

test_case_num = int(data())
test_case = []
answer = []


def make_test_case():

    n = int(data())
    tc_counter = collections.Counter(list(data().strip().split()[1] for _ in range(n)))

    return list(tc_counter.values())


def get_num_of_cases(costume_count_list):
    result = 1
    for count in costume_count_list:
        result *= (count + 1)
    return result - 1  # 알몸인 경우 제외


for _ in range(test_case_num):
    test_case.append(make_test_case())

for tc in test_case:
    answer.append(get_num_of_cases(tc))

print("\n".join(map(str, answer)))
