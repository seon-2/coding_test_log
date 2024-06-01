# 주어진 단어가 몇개의 크로아티아 알파벳으로 이루어져 있는지 출력하기

import sys
import re

# 입력을 받을 때 stdin에서 읽음
read = sys.stdin.read
word = read().strip()

# 크로아티아 알파벳 패턴 정의
cro_alpha_patterns = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 패턴 매칭을 통해 크로아티아 알파벳을 단일 문자로 변환
for pattern in cro_alpha_patterns:
    word = word.replace(pattern, 'X')

# 변환된 단어의 길이 출력
print(len(word))
