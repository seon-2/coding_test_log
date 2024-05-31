# 주어진 알고리즘의 시간복잡도는 O(n^3)
# 3중 for문이 각각 1~(n-2), (i+1)~(n-1), (j+1)~n 수행한다.
# (i, j, k)는 (1, 2, 3~7) (1, 3, 4~7) ... (2, 3~7)...(5,6~7) (6,7)이 된다.

from sys import stdin as s

n = int(s.readline().rstrip())

total_sum = 0
for i in range(1, n):
    total_sum += i * (n-1-i)
print(total_sum)
print(3)

# 5+..+1 + 4+..+1 + + 3+..+1 + 2+1 +1
# (1*5) + (2*4) + ...(5*1)