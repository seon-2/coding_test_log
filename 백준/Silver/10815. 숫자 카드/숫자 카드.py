from sys import stdin

N = int(stdin.readline())
card_set = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
numbers = map(int, stdin.readline().split())

print(' '.join('1' if num in card_set else '0' for num in numbers))