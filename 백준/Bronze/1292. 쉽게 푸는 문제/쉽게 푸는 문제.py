# 누적합

N, M = map(int, input().split())


def make_sequence(M):
    sequence = []
    i = 1
    while len(sequence) < M+1:
        for j in range(i):
            sequence.append(i)
        i += 1
    return sequence


def get_prefix_sum(m, sequence):
    prefix_list = [0] * (m+1)
    prefix_list[0] = sequence[0]
    for i in range(1, m+1):
        prefix_list[i] = prefix_list[i-1] + sequence[i]
    return prefix_list


sequence = make_sequence(M)
prefix_list = get_prefix_sum(M, sequence)

# 수열에서 N번째 숫자부터 M번째 숫자까지의 합
if N == 1:
    print(prefix_list[M-1])
else:
    print(prefix_list[M-1] - prefix_list[N-2])
