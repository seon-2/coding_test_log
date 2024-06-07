from sys import stdin

N = int(stdin.readline())
coordinates = list(map(int, stdin.readline().split()))
sorted_coord = sorted(set(coordinates))
coord_dict = {coord: idx for idx, coord in enumerate(sorted_coord)}

result = [coord_dict[coord] for coord in coordinates]
print(*result)