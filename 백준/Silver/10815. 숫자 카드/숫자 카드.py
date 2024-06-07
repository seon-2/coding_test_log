from sys import stdin

N = int(stdin.readline())
card_set = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

result = []
for number in numbers:
    result.append(1 if number in card_set else 0)

print(*result)