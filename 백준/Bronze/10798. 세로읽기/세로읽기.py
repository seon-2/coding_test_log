# 가로로 입력 받아 세로로 출력하기

import sys
# sys.stdin=open("input.txt","rt")
input = sys.stdin.read

lines = input().strip().split('\n')
result = []
max_length = max(len(line) for line in lines)

# 세로로 읽기
for i in range(max_length):
    for line in lines:
        if i < len(line):
            result.append(line[i])

print(''.join(result))