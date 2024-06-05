# 1. 첫 번째 원소를 뽑아낸다. popleft()
# 2. 왼쪽으로 한 칸 이동시킨다. a = popleft(),  append(a) 
# 3. 오른쪽으로 한 칸 이동시킨다. a = pop(), appendleft(a) 

import sys
from collections import deque
# sys.stdin = open("input.txt","rt")
data = sys.stdin.readline

deck = deque() # 양방향 순환 큐
N, M = map(int, data().split())
targets = list(map(int, data().split())) # 뽑아내려고 하는 원소의 위치
answer = 0

for index in range(N): # 양방향 순환 큐 만들기
    deck.append(index+1)

for target in targets:
    while len(deck) > N-M: # 뽑아낼 때까지
        if target == deck[0]:
            deck.popleft()
            break

        if deck.index(target) < len(deck) / 2: # 앞쪽이 가까움
            deck.append(deck.popleft()) # 2번
        else:
            deck.appendleft(deck.pop()) # 3번
        answer += 1

print(answer)