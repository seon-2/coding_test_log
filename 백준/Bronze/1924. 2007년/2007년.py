# 2007년 x월 y일은 무슨 요일?
# 1월 31일은 수요일, 2월 1일은 목요일
# 이전 달 마지막날의 인덱스만큼 더해주면 됨
# 더해줄 값 먼저 찾기 plus 리스트

from sys import stdin as s

# s=open("input.txt","rt")

x, y = map(int, s.readline().split())

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
plus = [0]
# plus = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5, 1]

for i in range (0, 12):
    plus.append((months[i] + plus[i]) % 7)

print(days[(y + plus[x-1])% 7])


