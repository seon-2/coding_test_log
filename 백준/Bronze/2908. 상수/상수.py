# 문자열 거꾸로 만들어서 크기 비교

from sys import stdin as s

A, B = input().split()
reverse_A = A[::-1]
reverse_B = B[::-1]

print(reverse_A if reverse_A > reverse_B else reverse_B)