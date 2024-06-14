from sys import stdin as s

n = int(s.readline().strip())
hills = list(map(int, s.readline().strip().split()))

height = hills[0]
answer = 0
count = 0

for i in range(1, n):
    if hills[i] < height:
        count += 1
    else:
        height = hills[i]
        answer = max(answer, count)
        count = 0

answer = max(answer, count) # 내림차순으로 정렬된 경우를 고려

print(answer)