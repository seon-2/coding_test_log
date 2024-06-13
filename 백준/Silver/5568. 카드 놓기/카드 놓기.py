from itertools import permutations

n = int(input())
k = int(input())
numbers = [input().strip() for _ in range(n)]

unique_numbers = set()

for perm in permutations(numbers, k):
    combined_number = ''.join(perm)
    unique_numbers.add(combined_number)

print(len(unique_numbers))
