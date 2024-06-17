N, M = map(int, input().split())

# 수열과 누적합을 동시 생성
def make_sequence_and_prefix_sum(m):
    sequence = []
    prefix_sum = [0] * (m + 1)
    current_number = 1
    index = 1
    
    while index <= m:
        for _ in range(current_number):
            if index > m:
                break
            sequence.append(current_number)
            prefix_sum[index] = prefix_sum[index - 1] + current_number
            index += 1
        current_number += 1

    return prefix_sum


prefix_sum = make_sequence_and_prefix_sum(M)

# 구간 합 계산
if N == 1:
    print(prefix_sum[M])
else:
    print(prefix_sum[M] - prefix_sum[N - 1])
