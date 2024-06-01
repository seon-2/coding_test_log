# 주어진 끝말잇기 기록에서 ?가 있는 위치를 찾는다.
# ? 앞의 단어의 끝 글자와 ? 뒤의 단어의 첫 글자를 찾는다.
# 후보 단어 중에서 위의 조건을 만족하는 단어를 찾는다.
# 이 단어가 이미 기록에 있는지 확인하여 중복되지 않게 한다.

import sys

# 입력을 받을 때 stdin에서 읽음
read = sys.stdin.read
ipt = read().strip().split("\n")

# 입력 데이터 파싱
N = int(ipt[0])
records = ipt[1:N+1]
M = int(ipt[N+1])
candidates = ipt[N+2:N+2+M]

# '?'의 위치 찾기
question_index = records.index('?')

# '?' 앞 단어의 끝 글자와 '?' 뒤 단어의 첫 글자 찾기
if question_index > 0:
    start_char = records[question_index - 1][-1]
else:
    start_char = None

if question_index < N - 1:
    end_char = records[question_index + 1][0]
else:
    end_char = None

# 후보 단어 중에서 올바른 단어 찾기
for candidate in candidates:
    if (start_char is None or candidate[0] == start_char) and \
       (end_char is None or candidate[-1] == end_char) and \
       (candidate not in records):
        print(candidate)
        break
