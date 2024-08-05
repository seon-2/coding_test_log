from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

count = Counter(array)
print(' '.join(str(count[target]) for target in targets))