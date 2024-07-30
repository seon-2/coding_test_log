import math

N = int(input())

if N == 1:
    print(1)
else:
    n = math.ceil((3 + math.sqrt(12*N - 3)) / 6)
    print(n)