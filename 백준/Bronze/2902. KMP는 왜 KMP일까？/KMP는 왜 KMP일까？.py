# Knuth-Morris-Pratt 을 KMP로 줄여서 출력하기

import sys

# s = open("input.txt", "rt")  # 입력 파일을 읽는 경우에만 필요
input = sys.stdin.read  # 입력을 받을 때 stdin에서 읽음

memo = input().strip().split("-")
answer = ''.join([word[0] for word in memo])
print(answer)
