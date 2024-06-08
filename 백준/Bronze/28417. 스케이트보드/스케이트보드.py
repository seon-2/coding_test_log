# [0], [1] 중에서 큰거 + [2:7] 중에서 상위 2개 = 최종 점수

from sys import stdin as s
from heapq import *


def get_final_score(score):
    final_score = 0
    final_score += score[0] if score[0] > score[1] else score[1]
    heap = [-x for x in score[2:7]]
    heapify(heap)
    final_score -= heappop(heap)
    final_score -= heap[0]
    return final_score


number_of_people = int(s.readline())
score_list = [list(map(int, s.readline().split())) for _ in range(number_of_people)]

print(max(get_final_score(score) for score in score_list))