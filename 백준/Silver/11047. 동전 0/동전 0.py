import sys

input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
K = int(data[1])
coins = list(map(int, data[2:]))

answer = 0

for i in range(N - 1, -1, -1):
    answer += K // coins[i]
    K = K % coins[i]

print(answer)