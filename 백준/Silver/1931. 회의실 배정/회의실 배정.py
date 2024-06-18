import sys

N = int(sys.stdin.readline().strip())
input_list = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    input_list.append((start, end))

input_list.sort(key=lambda x: (x[1], x[0]))

answer = 0
temp = 0

for start, end in input_list:
    if start >= temp:
        answer += 1
        temp = end

print(answer)