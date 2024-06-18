N = int(input())

# 불가능한 경우 : 4, 7
if N == 4 or N == 7:
    print(-1)
else:
    cnt = N // 5
    if N % 5 == 1 or N % 5 == 3:
        cnt += 1
    elif N % 5 == 2 or N % 5 == 4:
        cnt += 2
    print(cnt)
