from sys import stdin as s
from itertools import combinations

N, S = map(int, s.readline().strip().split())
numbers = list(map(int, s.readline().strip().split()))
answer = 0
# 모든 부분수열을 만들고 합을 구해서 경우의 수 찾기
for i in range(1, N+1):
    for seq in list(combinations(numbers, i)):
        if sum(seq) == S:
            answer += 1

print(answer)