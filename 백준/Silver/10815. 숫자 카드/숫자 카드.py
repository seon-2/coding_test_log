from sys import stdin

N = int(input())
card_set = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

result = []

for number in numbers:
    result.append(1 if number in card_set else 0)

print(' '.join(map(str, result)))