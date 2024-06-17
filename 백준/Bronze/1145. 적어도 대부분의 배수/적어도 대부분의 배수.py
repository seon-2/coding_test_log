from sys import stdin
from itertools import combinations
import math

numbers = list(map(int, stdin.read().strip().split()))

# 최소값 초기화
min_lcm = float('inf')

# 3개의 수를 조합해 최소 공배수를 계산하며 최소값 갱신
for combi_num in combinations(numbers, 3):
    lcm_value = math.lcm(*combi_num)
    if lcm_value < min_lcm:
        min_lcm = lcm_value

print(min_lcm)
