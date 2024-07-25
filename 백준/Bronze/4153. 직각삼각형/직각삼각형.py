from sys import stdin as s

while True:
    numbers = list(map(int, s.readline().strip().split()))
    longest = max(numbers)
    
    if longest == 0:
        break

    numbers.remove(longest)

    if longest**2 == numbers[0]**2 + numbers[1]**2:
        print("right")
    else:
        print("wrong")