import itertools
import math

def solution(numbers):
    num_set = set()
    
    # 모든 가능한 숫자 조합을 set에 추가
    for i in range(1, len(numbers) + 1):
        for perm in itertools.permutations(numbers, i):
            num = int(''.join(perm))
            num_set.add(num)
    
    # 소수 판별 함수
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    # 가능한 숫자 중 소수만 찾아서 개수 세기
    prime_count = sum(1 for num in num_set if is_prime(num))
    
    return prime_count
