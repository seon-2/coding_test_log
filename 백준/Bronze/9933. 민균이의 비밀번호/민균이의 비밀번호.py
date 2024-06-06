# reverse 단어도 포함되어 있는 단어 찾기

import sys
from heapq import *
data = sys.stdin.readline

N = int(data())
words = [data().strip() for _ in range(N)]

heapify(words)

while words:
    word = heappop(words)
    reversed_word = word[::-1]
    if word == reversed_word or reversed_word in words:
        print(len(word), word[len(word) // 2])
