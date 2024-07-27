from collections import Counter
from math import prod

def solution(clothes):
    clothes_counter = Counter(category for _, category in clothes)
    return prod(count + 1 for count in clothes_counter.values()) - 1