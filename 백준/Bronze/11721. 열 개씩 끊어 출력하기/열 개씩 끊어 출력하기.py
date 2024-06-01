# 10글자씩 끊어서 출력하기
import sys

input = sys.stdin.read  # 입력을 받을 때 stdin에서 읽음

words = input().strip()
print('\n'.join(words[i:i+10] for i in range(0, len(words), 10)))