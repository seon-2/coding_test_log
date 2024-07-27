# 주어진 수 N개 중에서 소수가 몇 개인지 출력

import math
from sys import stdin as s


N = int(input())
input_data = map(int, s.readline().split(" "))

def is_prime_numbers(N):
    if N == 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False

    return True


cnt = 0
for num in input_data:
    if is_prime_numbers(num):
        cnt += 1

print(cnt)
