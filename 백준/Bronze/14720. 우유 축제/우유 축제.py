from sys import stdin as s

N = int(input())
stores = list(map(int, s.readline().strip().split()))
count = 0
state = 0 # 0은 딸기우유, 1은 초코우유, 2는 바나나우유

for milk in stores:
    if milk == state:
        count += 1
        state = (state + 1) % 3

print(count)