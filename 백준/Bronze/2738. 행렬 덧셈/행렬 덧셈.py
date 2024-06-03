# 행렬 덧셈 구현

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

A = []
B = []

index = 2
for i in range(N):
    A.append([int(data[index + j]) for j in range(M)])
    index += M

for i in range(N):
    B.append([int(data[index + j]) for j in range(M)])
    index += M

result = []
for i in range(N):
    result.append([A[i][j] + B[i][j] for j in range(M)])

for row in result:
    print(" ".join(map(str, row)))
