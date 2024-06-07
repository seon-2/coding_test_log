# 술 소비가 가장 많은 학교이름 출력하기
# 힙 정렬 사용해서 최대값 찾기

import heapq
from sys import stdin as s
from heapq import *

test_case_number = int(s.readline().strip())
answers = []


# 입력 받기
def make_univ_list():
    univ_number = int(s.readline().strip())
    univ_list = []
    for _ in range(univ_number):
        univ_name, drink = map(str, s.readline().strip().split())
        univ_list.append([int(drink), univ_name])
    return univ_list


# 가장 큰 값 찾기(최대 힙)
def find_best_drinker(univ_list):
    max_heap = []
    for drink, univ_name in univ_list:
        heapq.heappush(max_heap, [-drink, univ_name])
    return heapq.heappop(max_heap)[1]


# 테스트 케이스 수만큼 반복
for _ in range(test_case_number):
    univ_list = make_univ_list()
    answers.append(find_best_drinker(univ_list))

# 정답 출력
print("\n".join(answers))
