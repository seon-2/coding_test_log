# 전공 평점 구하기
# 일단, 입력 받을 때, 학점이랑 등급만 가져오고, 등급이 P나 F인 것은 제외한다.
# 학점 * 등급을 누적해서 계산하고 과목수로 나눈다. 실수가 나와야 한다.

from sys import stdin as s
# s=open("input.txt","rt")

grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

score_sum = 0
class_sum = 0

data = [list(map(str, s.readline().split())) for _ in range(20)]
major_list = [[x[1], x[2]] for x in data if x[2] != 'P']

for ml in major_list:
    class_sum += float(ml[0])
    score_sum += (float(ml[0]) * grade[ml[1]])

print("{:.6f}".format(score_sum / class_sum))