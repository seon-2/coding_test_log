# --- 3번 소수 단어
# 1. 단어의 합 구하기 (a=1, z=26, A=27, Z=52)
# 아스키코드 a=97, z=122, A=65, Z=90)
# 2. 소수 판별하기

import sys
# sys.stdin = open("input.txt","rt")
read = sys.stdin.readline
word = read().strip()
number = 0

# 단어 합 구하기
for char in word: 
    if ord(char) > 96: # 소문자
        number += ord(char) - 96
    else: # 대문자
        number += ord(char) - 38

# 소수 판별 함수
def is_prime_num(number):
    for i in range(2, int(number // 1/2) + 1):
        if number % i == 0: # 나누어 떨어지면 소수 아님
            return False

    # 다 안 나누어 떨어지면
    return True

print("It is a prime word." if is_prime_num(number) else "It is not a prime word.")
