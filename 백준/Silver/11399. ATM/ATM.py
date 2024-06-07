# 작은 순서대로 누적합

from sys import stdin as s

N = int(s.readline())
times = sorted(map(int, s.readline().strip().split()))

def prefix_sum(N):
    prefix_list = [0] * N
    prefix_list[0] = times[0]

    for i in range(1, N):
        prefix_list[i] = prefix_list[i-1] + times[i]

    return prefix_list

print(sum(prefix_sum(N)))