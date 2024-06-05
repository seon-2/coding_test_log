# 마지막 막대부터 시작해서 큰 것만 보임. 크면 기준 막대 업데이트

import sys
# sys.stdin = open("input.txt","rt")
read = sys.stdin.readline

N = int(read())
stick = [(int(read().strip())) for _ in range(N)]
last = stick.pop()
answer = 1

for _ in range(N-1):
    now = stick.pop()
    if now > last:
        answer += 1
        last = now

print(answer)