# B의 각 숫자가 A안에 존재하는지 출력. 존재하면 1, 아니면 0

import sys
import collections
data = sys.stdin.readline

N = int(data())
counter_A = collections.Counter(list(map(int, data().strip().split())))
M = int(data())
num_list = list(map(int, data().strip().split()))
answer = []

def is_num_in_A(num):
    if num in counter_A:
        return 1
    else:
        return 0


for num in num_list:
    answer.append(is_num_in_A(num))

print("\n".join(map(str, answer)))
