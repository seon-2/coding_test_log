def hanoi(n, start, end, mid):
    if n == 1: # 1이면 바로 출발에서 목표로
        return [[start, end]]
    else:
        return (hanoi(n-1, start, mid, end) + # n-1개의 원판을 출발 기둥에서 중간 기둥으로 옮기기
                [[start, end]] + # n번째 (가장 큰) 원판을 출발 기둥에서 목표 기둥으로 옮기기
                hanoi(n-1, mid, end, start)) # n-1개의 원판을 중간 기둥에서 목표 기둥으로 옮기기

def solution(n):
    return hanoi(n, 1, 3, 2)