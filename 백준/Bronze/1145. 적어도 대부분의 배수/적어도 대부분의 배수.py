from sys import stdin as s
from itertools import combinations
import math

numbers = list(map(int, s.readline().strip().split()))
combi = list(combinations(numbers, 3))
result = []

for combi_num in combi:
    result.append(math.lcm(combi_num[0], combi_num[1], combi_num[2]))

print(min(result))