# --- 2번 단어순서 뒤집기
# 단어를 하나씩 pop() 하기. N=5이기 때문에 시간 복잡도 신경 안 씀

import sys
# sys.stdin = open("input.txt","rt")
read = sys.stdin.readline

N = int(read().strip())
cases = [read().strip().split() for _ in range(N)]

for index, case in enumerate(cases):
    answer = ""
    while case:
        answer += case.pop() + " "
    print(f"Case #{index+1}: {answer}")