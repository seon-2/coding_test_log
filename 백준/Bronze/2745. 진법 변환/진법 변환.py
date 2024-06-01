# B진법 수 N을 10진법으로 바꿔 출력하기

import sys

#sys.stdin = open("input.txt", "rt")  # 입력 파일을 읽는 경우에만 필요
input = sys.stdin.read  # 입력을 받을 때 stdin에서 읽음
B, N = input().strip().split()
print(int(B, int(N)))

