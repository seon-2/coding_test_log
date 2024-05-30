# 사칙연산

from sys import stdin as s

N = int(s.readline().rstrip())
data = list(map(int, s.readline().split()))
print(sum(data) / max(data) * 100 / N)