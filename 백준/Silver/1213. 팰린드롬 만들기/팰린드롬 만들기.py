import sys
import collections

# 입력을 받을 때 stdin에서 읽음
read = sys.stdin.read
word = list(read().strip())
char_count = collections.Counter(word)

# 홀수 개수의 문자가 몇 개인지 확인
odd_count = 0
mid_char = ""
left_half = []

for char, count in sorted(char_count.items()):  # 사전순으로 정렬
    if count % 2 != 0:
        odd_count += 1
        mid_char = char
    
    # 절반씩만 left_half에 추가 (사전순으로 추가됨)
    left_half.append(char * (count // 2))

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    # 사전순으로 가장 앞서는 팰린드롬 생성
    left_half_str = ''.join(left_half)
    if mid_char:
        answer = left_half_str + mid_char + left_half_str[::-1]
    else:
        answer = left_half_str + left_half_str[::-1]
    print(answer)
