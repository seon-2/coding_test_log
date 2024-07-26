# 티셔츠는 남아도 되지만 부족해서는 안 되고 신청한 사이즈대로 나눠주어야 함
# 펜은 남거나 부족해서는 안 되고 정확히 참가자 수만큼 준비되어야 함
import math
from sys import stdin as s
# s = open("input.txt", "rt")

N = int(s.readline())  # 전체 참가자 수
numbers = list(map(int, s.readline().strip().split(" ")))  # 사이즈 별 신청자 수
T, P = map(int, s.readline().strip().split(" "))  # 티셔츠 묶음 수, 펜 묶음 수

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지?
answers = [math.ceil(num / T) for num in numbers]

# 펜 최대 몇 묶음, 한 자루씩 몇 개?
print(sum(answers))
print(N // P, N % P)
