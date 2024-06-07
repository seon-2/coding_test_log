# 리스트에 포함되지 않은 가장 작은 자연수 찾기
# 리스트에서 가장 작은 수를 뽑자.
# 그게 1이 아니라면, 1을 출력
# 1이라면, 하나씩 늘려가면서 pop하면서 찾기
# 1차 티켓에서 빈공간이 없는 경우 체크하기

from sys import stdin as s
from heapq import *

ticket_number = int(s.readline().strip())
tickets = list(map(int, s.readline().split()))

heapify(tickets)


def get_my_ticket_number(tickets):
    min_ticket_number = heappop(tickets)

    if min_ticket_number != 1: # 1차 티켓에서 1번이 없는 경우
       return 1

    else: # 1차 티켓의 빈 번호 중 가장 작은 값 찾기
        my_ticket_number = 2
        while tickets: # 티켓이 있는 동안
            min_ticket_number = heappop(tickets)

            if my_ticket_number < min_ticket_number:
                return my_ticket_number

            my_ticket_number += 1

    return my_ticket_number # 1차 티켓에 빈 번호가 없는 경우

print(get_my_ticket_number(tickets))