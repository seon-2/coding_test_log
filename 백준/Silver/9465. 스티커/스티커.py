from sys import stdin as s

tc_num = int(s.readline())

def get_max_score():
    n = int(s.readline())
    top = list(map(int, s.readline().strip().split()))
    bottom = list(map(int, s.readline().strip().split()))

    dp_top = [0] * n
    dp_bottom = [0] * n

    dp_top[0] = top[0]
    dp_bottom[0] = bottom[0]

    for i in range(1, n):
        dp_top[i] = top[i] + max(dp_bottom[i-1], (i > 1) * dp_bottom[i-2])
        dp_bottom[i] = bottom[i] + max(dp_top[i-1], (i > 1) * dp_top[i-2])

    print(max(dp_top[n-1], dp_bottom[n-1]))

for i in range(tc_num):
    get_max_score()