# 1-6 눈을 가진 주사위 3개 던져서 상금 계산하기
# 1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

from sys import stdin as s

# s=open("input.txt","rt")

A, B, C = map(int, s.readline().split())
prize = 0

if A == B == C: # 1) 같은 눈 3개
    prize = 10000 + A * 1000
elif A != B and A != C and B != C: # 3) 모두 다른 눈일 때
    prize = max(A, B, C) * 100
else: # 2) 같은 눈 2개
    if A == B or A == C:
        prize = 1000 + A * 100
    else:
        prize = 1000 + B * 100

print(prize)