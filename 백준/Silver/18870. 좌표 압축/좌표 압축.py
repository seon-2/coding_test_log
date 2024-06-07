# 나보다 작은 애들의 개수

from sys import stdin as s

N = int(s.readline())
coordinates = list(map(int, s.readline().strip().split()))
coord_set = set(coordinates)
sorted_coord = sorted(list(coord_set))
coord_dict = {}

for index, cord in enumerate(sorted_coord):
    coord_dict[cord] = index

result = []
for coord in coordinates:
    result.append(coord_dict[coord])

print(' '.join(map(str, result)))