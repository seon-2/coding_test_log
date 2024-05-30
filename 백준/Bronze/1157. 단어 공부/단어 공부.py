# 다 대문자로 바꾸고
# Counter의 most_common 사용하기

from sys import stdin as s
from collections import Counter

str = s.readline().rstrip()

s_list = list(str.upper()) # ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'I']
counter = Counter(s_list).most_common() # Counter({'I': 4, 'S': 4, 'M': 1, 'P': 1})

if len(counter) == 1:
    print(counter[0][0])
else:
    if counter[0][1] == counter[1][1]:
        print("?")
    else:
        print(counter[0][0])