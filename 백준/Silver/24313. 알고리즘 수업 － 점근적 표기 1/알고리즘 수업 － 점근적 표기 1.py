a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 > c:
    print(0)
elif a1 == c:
    if a0 <= 0:
        print(1)
    else:
        print(0)
else:
    limit = a0 / (c - a1)
    if n0 >= limit:
        print(1)
    else:
        print(0)