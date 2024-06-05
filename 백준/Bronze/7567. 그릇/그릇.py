import sys
# sys.stdin = open("input.txt", "rt")
data = sys.stdin.readline().strip()

height = 10

previous_plate = data[0]

for current_plate in data[1:]:
    if previous_plate == current_plate:
        height += 5
    else:
        height += 10
    previous_plate = current_plate

print(height)
