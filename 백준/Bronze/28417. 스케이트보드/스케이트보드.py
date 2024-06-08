# [0], [1] 중에서 큰거 + [2:7] 중에서 상위 2개 = 최종 점수

from sys import stdin as s

number_of_people = int(input())
score_list = []
final_score_list = []

# 입력
for _ in range(number_of_people):
    score_list.append(list(map(int, s.readline().split())))


def get_final_score(score):
    final_score = 0
    final_score += score[0] if score[0] > score[1] else score[1]
    sorted_score = sorted(score[2:7])
    final_score += sorted_score[-1] + sorted_score[-2]
    return final_score


for score in score_list:
    final_score_list.append(get_final_score(score))

print(max(final_score_list))