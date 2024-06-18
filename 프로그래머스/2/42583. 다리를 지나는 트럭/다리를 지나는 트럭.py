from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_deck = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 다리를 0으로 초기화
    total_weight = 0  # 현재 다리 위 트럭 무게 합
    time = 0

    while truck_deck or sum(bridge) > 0:
        time += 1
        total_weight -= bridge.popleft()

        if truck_deck:
            if total_weight + truck_deck[0] <= weight:
                truck = truck_deck.popleft()
                total_weight += truck
                bridge.append(truck)
            else:
                bridge.append(0)

    return time  # 마지막 트럭이 다리를 건너는 시간 추가