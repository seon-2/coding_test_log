def count_pn_occurrences(N, M, S):
    pattern_length = 2 * N + 1
    count = 0
    i = 0

    while i <= M - pattern_length:
        if S[i:i + pattern_length] == "I" + "OI" * N:
            count += 1
            i += 2  # IOI 패턴에서 O 다음부터 다시 검사 시작
        else:
            i += 1

    return count

# 입력 처리
N = int(input().strip())
M = int(input().strip())
S = input().strip()

# 결과 출력
print(count_pn_occurrences(N, M, S))
