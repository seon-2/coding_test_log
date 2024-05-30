# 문자열을 1개, 2개...len개 만큼 자르기

from sys import stdin as s

str = (s.readline().rstrip())
str_set = set()

for i in range(1, len(str)+1):
    for j in range(0, len(str)+1):
        str_set.add(str[j:i:])

print(len(str_set)-1)