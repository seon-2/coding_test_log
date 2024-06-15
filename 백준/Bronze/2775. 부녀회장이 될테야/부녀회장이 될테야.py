from sys import stdin as s

def solution(k, n):
    # 0층의 각 호실에 살고 있는 사람 수 초기화
    apart = [x for x in range(1, n + 1)]

    # 1층부터 k층까지 계산
    for floor in range(1, k + 1):
        temp = []  # 해당 층의 각 호실에 살고 있는 사람 수를 임시로 저장할 리스트
        sum_val = 0  # 이전 층의 1호부터 현재 호실까지 사람 수의 합
        for room in range(n):
            sum_val += apart[room]  # 이전 층의 1호부터 현재 호실까지 사람 수 합산
            temp.append(sum_val)  # 현재 호실에 살고 있는 사람 수를 임시 리스트에 저장
        apart = temp[:]  # 해당 층의 각 호실에 살고 있는 사람 수 정보를 apart에 저장

    return apart[-1]  # k층 n호에 살고 있는 사람 수 반환


T = int(s.readline().strip())  # 테스트 케이스 수
for _ in range(T):
    k = int(s.readline().strip())  # 층
    n = int(s.readline().strip())  # 호실
    print(solution(k, n))